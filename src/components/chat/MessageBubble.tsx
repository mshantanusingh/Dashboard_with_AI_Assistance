"use client";

import { ChatMessage } from "@/lib/types";
import { cn } from "@/lib/utils";
import { User, Bot, Wrench } from "lucide-react";
import ReactMarkdown from 'react-markdown';

export function MessageBubble({ message }: { message: ChatMessage }) {
  const isUser = message.role === "user";

  return (
    <div className={cn("flex w-full gap-3 animate-slide-up", isUser ? "flex-row-reverse" : "flex-row")}>
      <div className={cn("flex-shrink-0 w-7 h-7 rounded-full flex items-center justify-center mt-1", 
        isUser ? "bg-white text-black" : "bg-cyan-500/10 border border-cyan-500/20 text-cyan-400"
      )}>
        {isUser ? <User className="w-4 h-4" /> : <Bot className="w-4 h-4" />}
      </div>
      
      <div className="flex flex-col gap-1 max-w-[80%]">
        {message.toolCalls && message.toolCalls.length > 0 && (
          <div className="flex flex-col gap-1 mb-2">
            {message.toolCalls.map((tc, idx) => (
              <div key={idx} className="flex items-center gap-1.5 text-[10px] text-neutral-400 bg-black/40 px-2 py-1.5 rounded-lg border border-white/5 w-fit">
                <Wrench className="w-3 h-3 text-neutral-500" />
                <span>Used <span className="font-medium text-neutral-300">{tc.server}</span> server to run <span className="font-mono text-cyan-400">{tc.tool}</span></span>
              </div>
            ))}
          </div>
        )}
        
        <div className={cn("px-4 py-3 text-sm leading-relaxed", 
          isUser ? "bg-white text-black rounded-2xl rounded-tr-sm" : "bg-white/[0.03] border border-white/5 text-neutral-200 rounded-2xl rounded-tl-sm chat-markdown"
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
