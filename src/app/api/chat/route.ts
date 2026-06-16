/* ─── Chat API Route ─────────────────────────────────────────────────────────
 * POST /api/chat
 * Receives user message + history, calls AI orchestrator, returns response.
 * Keeps the Gemini API key server-side (never exposed to browser).
 * ──────────────────────────────────────────────────────────────────────────── */

import { NextRequest, NextResponse } from "next/server";
import { orchestrateChat } from "@/lib/ai-orchestrator";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { message, history, persona } = body;

    if (!message || typeof message !== "string") {
      return NextResponse.json(
        { error: "Message is required and must be a string" },
        { status: 400 }
      );
    }

    const apiKey = process.env.GEMINI_API_KEY;
    if (!apiKey) {
      return NextResponse.json(
        {
          error: "GEMINI_API_KEY is not configured. Please add it to your .env.local file.",
          message: "⚠️ AI Assistant is not configured. Please set up your Gemini API key in the `.env.local` file to enable the AI chat feature.\n\nYou can get a free API key from [Google AI Studio](https://aistudio.google.com/apikey).",
          toolCalls: [],
        },
        { status: 200 } // Return 200 so the chat UI can display the message
      );
    }

    const conversationHistory = Array.isArray(history) ? history : [];

    const result = await orchestrateChat(message, conversationHistory, apiKey, persona);

    return NextResponse.json(result);
  } catch (error) {
    console.error("Chat API error:", error);

    const errorMessage =
      error instanceof Error ? error.message : "Unknown error occurred";

    return NextResponse.json(
      {
        error: errorMessage,
        message: `Sorry, I encountered an error processing your request: ${errorMessage}. Please try again.`,
        toolCalls: [],
      },
      { status: 500 }
    );
  }
}
