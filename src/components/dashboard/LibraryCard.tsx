"use client";

import { useMCPData } from "@/hooks/useMCPData";
import { usePersona } from "@/context/PersonaContext";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Skeleton } from "@/components/ui/Skeleton";
import { Book, Library } from "lucide-react";
import { BookInfo } from "@/lib/types";

export function LibraryCard() {
  const { activePersona } = usePersona();
  
  const { data, loading, error } = useMCPData<{ popular_books: BookInfo[] }>({
    server: "library",
    tool: "get_popular_books",
    parameters: { limit: 3, student_id: activePersona.id },
  });

  return (
    <Card className="bento-item-wide overflow-hidden flex flex-col h-full bg-black/40 border border-[var(--border-subtle)] shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]">
      <CardHeader className="pb-2">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-[var(--accent-indigo)]/10 rounded-lg">
            <Library className="w-5 h-5 text-[var(--accent-indigo)]" />
          </div>
          <div>
            <CardTitle className="text-lg">Digital Library</CardTitle>
            <CardDescription className="text-xs uppercase tracking-wider text-[var(--text-muted)]">Trending Titles</CardDescription>
          </div>
        </div>
      </CardHeader>
      <CardContent className="flex-1 overflow-hidden p-0 relative">
        <div className="flex gap-4 overflow-x-auto no-scrollbar px-6 pb-6 pt-2 snap-x snap-mandatory">
          {loading ? (
            Array(4).fill(0).map((_, i) => (
              <div key={i} className="flex-shrink-0 w-28 snap-center">
                <Skeleton className="h-36 w-full rounded-md border border-white/5" />
                <Skeleton className="h-3 w-3/4 mt-3" />
                <Skeleton className="h-2 w-1/2 mt-2" />
              </div>
            ))
          ) : error ? (
            <div className="text-sm text-[var(--accent-rose)] px-6">Failed to load library data</div>
          ) : data?.popular_books ? (
            data.popular_books.map((book, i) => {
              const colors = [
                "bg-neutral-800/80 border-neutral-700/50",
                "bg-neutral-800/60 border-neutral-700/50",
                "bg-neutral-900/80 border-neutral-800/50",
              ];
              const theme = colors[book.title.length % colors.length];

              return (
                <div key={book.id} className="flex-shrink-0 w-28 snap-center group cursor-pointer">
                  {/* Book Cover */}
                  <div className={`relative h-36 rounded-md border shadow-sm transition-transform duration-300 group-hover:-translate-y-1 group-hover:bg-neutral-800 ${theme} p-3 flex flex-col justify-between overflow-hidden`}>
                    {/* Minimalist Spine highlight */}
                    <div className="absolute top-0 bottom-0 left-0 w-0.5 bg-white/5" />
                    
                    <h4 className="text-[11px] font-medium text-neutral-200 leading-tight mt-1 z-10">{book.title}</h4>
                    <Book className="w-4 h-4 text-neutral-500 self-end mb-1 z-10" />
                  </div>
                  
                  {/* Meta */}
                  <div className="mt-3">
                    <p className="text-xs text-neutral-400 truncate font-medium">{book.author}</p>
                    <div className="flex items-center gap-1.5 mt-1.5">
                      <div className={`w-1.5 h-1.5 rounded-full ${book.available ? 'bg-emerald-500/80' : 'bg-neutral-600'}`} />
                      <span className="text-[10px] text-neutral-300 font-medium">{book.available ? "Available" : "Checked Out"}</span>
                    </div>
                  </div>
                </div>
              );
            })
          ) : (
            <div className="text-sm text-[var(--text-muted)] px-6">No books available</div>
          )}
        </div>
        
        {/* Fade gradients for scroll edges */}
        <div className="absolute top-0 bottom-0 left-0 w-6 bg-gradient-to-r from-black/80 to-transparent pointer-events-none" />
        <div className="absolute top-0 bottom-0 right-0 w-6 bg-gradient-to-l from-black/80 to-transparent pointer-events-none" />
      </CardContent>
    </Card>
  );
}
