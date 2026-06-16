/* ─── AI Orchestrator ────────────────────────────────────────────────────────
 * The brain of the system. Orchestrates:
 * 1. Tool discovery from all MCP servers
 * 2. LLM function-calling to route queries to the right tools
 * 3. Tool execution and result aggregation
 * 4. Natural language response synthesis
 *
 * Supports Google Gemini API with function calling.
 * ──────────────────────────────────────────────────────────────────────────── */

import { GoogleGenerativeAI, FunctionDeclaration, SchemaType, Tool as GeminiTool } from "@google/generative-ai";
import { discoverAllTools, executeTool, findServerForTool } from "./mcp-client";
import { MCPToolSchema, MCPServerConfig, ToolCallInfo } from "./types";

// ─── Types ──────────────────────────────────────────────────────────────────

export interface OrchestratorResponse {
  message: string;
  toolCalls: ToolCallInfo[];
}

// ─── Convert MCP Schema to Gemini Function Declarations ─────────────────────

function mcpSchemaToGemini(tool: MCPToolSchema, serverName: string): FunctionDeclaration {
  const properties: Record<string, any> = {};
  const required: string[] = [];

  const params = tool.parameters as {
    properties?: Record<string, { type: string; description: string; enum?: string[] }>;
    required?: string[];
  };

  if (params.properties) {
    for (const [key, prop] of Object.entries(params.properties)) {
      let schemaType: SchemaType;
      switch (prop.type) {
        case "integer":
          schemaType = SchemaType.INTEGER;
          break;
        case "number":
          schemaType = SchemaType.NUMBER;
          break;
        case "boolean":
          schemaType = SchemaType.BOOLEAN;
          break;
        case "array":
          schemaType = SchemaType.ARRAY;
          break;
        default:
          schemaType = SchemaType.STRING;
      }

      const propSchema: any = {
        type: schemaType,
        description: prop.description || key,
      };

      if (prop.enum) {
        propSchema.enum = prop.enum;
      }

      properties[key] = propSchema;
    }
  }

  if (params.required) {
    required.push(...params.required);
  }

  // Prefix tool name with server name to disambiguate across servers
  return {
    name: `${serverName}__${tool.name}`,
    description: `[${serverName.toUpperCase()} SERVER] ${tool.description}`,
    parameters: {
      type: SchemaType.OBJECT,
      properties: Object.keys(properties).length > 0 ? properties : { _dummy: { type: SchemaType.STRING, description: "No parameters needed" } as any },
      required: required.length > 0 ? required : undefined,
    },
  };
}

// ─── Main Orchestrator ──────────────────────────────────────────────────────

export async function orchestrateChat(
  userMessage: string,
  conversationHistory: { role: string; content: string }[],
  apiKey: string
): Promise<OrchestratorResponse> {
  // Step 1: Discover all available tools from MCP servers
  const toolsMap = await discoverAllTools();

  // Step 2: Build Gemini function declarations from MCP tool schemas
  const functionDeclarations: FunctionDeclaration[] = [];
  const toolServerMap: Map<string, { server: MCPServerConfig; toolName: string }> = new Map();

  for (const [serverName, { server, tools }] of toolsMap) {
    for (const tool of tools) {
      const geminiDecl = mcpSchemaToGemini(tool, serverName);
      functionDeclarations.push(geminiDecl);
      toolServerMap.set(`${serverName}__${tool.name}`, {
        server,
        toolName: tool.name,
      });
    }
  }

  // Step 3: Call Gemini with function-calling enabled
  const genAI = new GoogleGenerativeAI(apiKey);
  const model = genAI.getGenerativeModel({
    model: "gemini-2.5-flash",
    systemInstruction: `You are CampusAI, an intelligent assistant for a university campus. You help students find information about the library, cafeteria menus, campus events, and academic schedules.

You have access to real-time data from campus systems through tools. ALWAYS use the appropriate tools to answer questions — never make up information.

When multiple tools could be relevant, call ALL of them to give a comprehensive answer.

Guidelines:
- Be friendly, concise, and helpful
- Use emojis sparingly to make responses engaging
- Format responses with markdown for readability
- If a tool returns no results, tell the student honestly
- For time-sensitive queries (today's menu, upcoming events), use tools to get current data
- When showing schedules, format them as clean lists or tables`,
    tools: functionDeclarations.length > 0
      ? [{ functionDeclarations } as GeminiTool]
      : undefined,
  });

  // Format history for Gemini, ensuring the first message is from the user
  let formattedHistory = conversationHistory
    .filter((msg) => msg.role !== "system")
    .map((msg) => ({
      role: msg.role === "assistant" ? "model" : "user",
      parts: [{ text: msg.content }],
    }));

  // Gemini requires the first message in history to be from the 'user'
  while (formattedHistory.length > 0 && formattedHistory[0].role === "model") {
    formattedHistory.shift();
  }

  const chat = model.startChat({
    history: formattedHistory,
  });

  // Step 4: Send message and handle function calls
  const toolCalls: ToolCallInfo[] = [];
  let result = await chat.sendMessage(userMessage);
  let response = result.response;

  // Handle multi-turn function calling
  let maxIterations = 5;
  while (maxIterations-- > 0) {
    const functionCallParts = response.candidates?.[0]?.content?.parts?.filter(
      (p) => "functionCall" in p
    );

    if (!functionCallParts || functionCallParts.length === 0) break;

    // Execute all function calls in parallel
    const functionResponses = await Promise.all(
      functionCallParts.map(async (part) => {
        const fc = part.functionCall!;
        const mappedTool = toolServerMap.get(fc.name);

        if (!mappedTool) {
          return {
            functionResponse: {
              name: fc.name,
              response: { error: `Unknown tool: ${fc.name}` },
            },
          };
        }

        // Remove dummy parameter if present
        const params = { ...fc.args } as Record<string, unknown>;
        delete params._dummy;

        // Execute tool on the appropriate MCP server
        const execResult = await executeTool(
          mappedTool.server,
          mappedTool.toolName,
          params
        );

        toolCalls.push({
          server: mappedTool.server.name,
          tool: mappedTool.toolName,
          parameters: params,
          result: execResult.result,
        });

        return {
          functionResponse: {
            name: fc.name,
            response: execResult.success
              ? execResult.result
              : { error: execResult.error },
          },
        };
      })
    );

    // Send function results back to Gemini for synthesis
    result = await chat.sendMessage(functionResponses as any);
    response = result.response;
  }

  // Step 5: Extract final text response
  const textContent = response.candidates?.[0]?.content?.parts
    ?.filter((p) => "text" in p)
    ?.map((p) => p.text)
    ?.join("\n") || "I couldn't process your request. Please try again.";

  return {
    message: textContent,
    toolCalls,
  };
}
