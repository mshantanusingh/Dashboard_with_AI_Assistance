"use client";

import { ChatMessage } from "@/lib/types";
import { cn } from "@/lib/utils";
import { User, Bot, Wrench } from "lucide-react";
import ReactMarkdown from 'react-markdown';

export function MessageBubble({ message }: { message: ChatMessage }) {
  const isUser = message.role === "user";

  return (
    <div className={cn("flex w-full gap-3 animate-slide-up", isUser ? "flex-row-reverse" : "flex-row")}>
      <div className={cn("flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center", 
        isUser ? "bg-[var(--accent-indigo)] text-white" : "bg-[var(--bg-secondary)] border border-[var(--border-subtle)] text-[var(--accent-cyan)]"
      )}>
        {isUser ? <User className="w-5 h-5" /> : <Bot className="w-5 h-5" />}
      </div>
      
      <div className="flex flex-col gap-1 max-w-[80%]">
        {message.toolCalls && message.toolCalls.length > 0 && (
          <div className="flex flex-col gap-1 mb-2">
            {message.toolCalls.map((tc, idx) => (
              <div key={idx} className="flex items-center gap-1.5 text-[10px] text-[var(--text-muted)] bg-[var(--bg-secondary)] px-2 py-1 rounded-md border border-[var(--border-subtle)] w-fit">
                <Wrench className="w-3 h-3" />
                <span>Used <span className="font-medium text-[var(--text-secondary)]">{tc.server}</span> server to run <span className="font-mono text-[var(--accent-violet)]">{tc.tool}</span></span>
              </div>
            ))}
          </div>
        )}
        
        <div className={cn("px-4 py-3 text-sm chat-markdown", 
          isUser ? "chat-bubble-user" : "chat-bubble-assistant"
        )}>
          {isUser ? (
            <p>{message.content}</p>
          ) : (
            <ReactMarkdown>{message.content}</ReactMarkdown>
          )}
        </div>
      </div>
    </div>
  );
}
