"use client";

import { useState, useRef, useEffect } from "react";
import { MessageSquare, X, Send, Sparkles } from "lucide-react";
import { useChat } from "@/hooks/useChat";
import { MessageBubble } from "./MessageBubble";
import { cn } from "@/lib/utils";

export function ChatWidget() {
  const [isOpen, setIsOpen] = useState(false);
  const [input, setInput] = useState("");
  const { messages, isLoading, sendMessage } = useChat();
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Auto-scroll and auto-focus
  useEffect(() => {
    if (isOpen) {
      messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
      setTimeout(() => inputRef.current?.focus(), 100);
    }
  }, [messages, isOpen, isLoading]);

  // Close on Escape
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") setIsOpen(false);
      // Cmd+K to open
      if ((e.metaKey || e.ctrlKey) && e.key === "k") {
        e.preventDefault();
        setIsOpen(prev => !prev);
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;
    
    sendMessage(input);
    setInput("");
  };

  const handleQuickAction = (text: string) => {
    sendMessage(text);
  };

  return (
    <>
      {/* Floating Action Button */}
      <button
        onClick={() => setIsOpen(true)}
        className={cn(
          "fixed bottom-8 right-8 px-5 py-3 rounded-full bg-white text-black shadow-[0_0_30px_rgba(255,255,255,0.3)] flex items-center gap-3 transition-transform hover:scale-105 active:scale-95 z-40 group",
          isOpen ? "scale-0 opacity-0 pointer-events-none" : "scale-100 opacity-100"
        )}
      >
        <Sparkles className="w-5 h-5 text-indigo-600 group-hover:animate-pulse" />
        <span className="font-semibold text-sm">Ask CampusAI</span>
        <div className="hidden sm:flex items-center gap-1 opacity-50 ml-2">
          <kbd className="font-sans text-[10px] px-1.5 py-0.5 rounded border border-black/20">⌘</kbd>
          <kbd className="font-sans text-[10px] px-1.5 py-0.5 rounded border border-black/20">K</kbd>
        </div>
      </button>

      {/* Full Screen Command Palette Overlay */}
      <div
        className={cn(
          "fixed inset-0 z-50 flex items-start justify-center pt-[10vh] px-4 transition-all duration-300",
          isOpen ? "opacity-100" : "opacity-0 pointer-events-none"
        )}
      >
        {/* Blurred Backdrop */}
        <div 
          className="absolute inset-0 bg-black/40 backdrop-blur-sm"
          onClick={() => setIsOpen(false)}
        />

        {/* Modal Window */}
        <div
          className={cn(
            "relative w-full max-w-3xl h-[70vh] min-h-[500px] glass-panel-extreme flex flex-col overflow-hidden transition-all duration-300 shadow-[0_0_100px_rgba(99,102,241,0.15)]",
            isOpen ? "scale-100 translate-y-0" : "scale-95 translate-y-4"
          )}
        >
          {/* Header */}
          <div className="flex items-center justify-between px-6 py-4 border-b border-white/10 bg-white/5">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-500 to-cyan-400 flex items-center justify-center shadow-lg shadow-indigo-500/20">
                <Sparkles className="w-4 h-4 text-white" />
              </div>
              <div>
                <h3 className="font-semibold text-sm text-white">CampusAI Command Center</h3>
                <p className="text-[10px] text-[var(--text-muted)] flex items-center gap-1.5 uppercase tracking-widest mt-0.5">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.6)]"></span> Online
                </p>
              </div>
            </div>
            <button 
              onClick={() => setIsOpen(false)}
              className="p-2 text-[var(--text-muted)] hover:text-white rounded-full hover:bg-white/10 transition-colors flex items-center gap-2"
            >
              <span className="text-[10px] uppercase tracking-wider hidden sm:inline-block">ESC</span>
              <X className="w-4 h-4" />
            </button>
          </div>

          {/* Messages Area */}
          <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-6 scroll-smooth no-scrollbar">
            {messages.length === 0 && !isLoading ? (
              <div className="flex-1 flex flex-col items-center justify-center opacity-50 space-y-4">
                <Sparkles className="w-12 h-12 text-white/20" />
                <p className="text-sm text-white/50">How can I help you today?</p>
              </div>
            ) : (
              messages.map((msg) => (
                <MessageBubble key={msg.id} message={msg} />
              ))
            )}
            
            {isLoading && (
              <div className="flex w-full gap-4 animate-fade-in flex-row">
                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 border border-white/10 flex items-center justify-center">
                  <Sparkles className="w-4 h-4 text-cyan-400 animate-pulse" />
                </div>
                <div className="bg-white/5 border border-white/10 px-5 py-4 rounded-2xl rounded-tl-sm text-sm">
                  <div className="typing-dots">
                    <span className="bg-white/50"></span><span className="bg-white/50"></span><span className="bg-white/50"></span>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input Area */}
          <div className="p-4 bg-black/40 backdrop-blur-md border-t border-white/10">
            {/* Quick Actions */}
            {messages.length <= 2 && !isLoading && (
              <div className="flex gap-2 overflow-x-auto no-scrollbar pb-3 mb-1">
                <button onClick={() => handleQuickAction("What's for dinner tonight?")} className="chip">🍽️ Dinner Menu</button>
                <button onClick={() => handleQuickAction("Are there any events happening right now?")} className="chip">📅 Live Events</button>
                <button onClick={() => handleQuickAction("Check if 'Database System Concepts' is available")} className="chip">📚 Find Book</button>
              </div>
            )}
            
            <form onSubmit={handleSubmit} className="relative flex items-center">
              <input
                ref={inputRef}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask CampusAI anything..."
                className="w-full bg-white/5 border border-white/10 rounded-xl py-4 pl-5 pr-14 text-base focus:outline-none focus:border-indigo-500/50 focus:bg-white/10 transition-all text-white placeholder:text-white/30"
                autoComplete="off"
              />
              <button
                type="submit"
                disabled={!input.trim() || isLoading}
                className="absolute right-2 p-2.5 bg-white text-black rounded-lg hover:bg-gray-200 disabled:opacity-20 disabled:hover:bg-white transition-all"
              >
                <Send className="w-4 h-4" />
              </button>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}
