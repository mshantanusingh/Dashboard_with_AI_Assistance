"use client";

import { useMCPData } from "@/hooks/useMCPData";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Skeleton } from "@/components/ui/Skeleton";
import { Book, Library } from "lucide-react";
import { BookInfo } from "@/lib/types";

export function LibraryCard() {
  const { data, loading, error } = useMCPData<{ popular_books: BookInfo[] }>({
    server: "library",
    tool: "get_popular_books",
    parameters: { limit: 3 },
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
              <div key={i} className="flex-shrink-0 w-32 snap-center">
                <Skeleton className="h-44 w-full rounded-md shadow-lg" />
                <Skeleton className="h-4 w-3/4 mt-3" />
                <Skeleton className="h-3 w-1/2 mt-1" />
              </div>
            ))
          ) : error ? (
            <div className="text-sm text-[var(--accent-rose)] px-6">Failed to load library data</div>
          ) : data?.popular_books ? (
            data.popular_books.map((book, i) => {
              // Generate a deterministic gradient based on book title
              const colors = [
                "from-indigo-500 to-cyan-400",
                "from-violet-500 to-fuchsia-500",
                "from-emerald-400 to-cyan-500",
                "from-amber-400 to-orange-500",
                "from-rose-500 to-pink-500"
              ];
              const gradient = colors[book.title.length % colors.length];

              return (
                <div key={book.id} className="flex-shrink-0 w-32 snap-center group cursor-pointer">
                  {/* Book Cover */}
                  <div className={`relative h-44 rounded-md shadow-[5px_5px_15px_rgba(0,0,0,0.5)] transition-transform duration-300 group-hover:-translate-y-2 group-hover:scale-105 bg-gradient-to-br ${gradient} p-3 flex flex-col justify-between overflow-hidden`}>
                    {/* Spine highlight */}
                    <div className="absolute top-0 bottom-0 left-0 w-1 bg-white/20" />
                    <div className="absolute top-0 bottom-0 left-1 w-0.5 bg-black/10" />
                    
                    <h4 className="text-[10px] font-bold text-white leading-tight mt-1 z-10 drop-shadow-md">{book.title}</h4>
                    <Book className="w-6 h-6 text-white/50 self-end mb-1 z-10" />
                  </div>
                  
                  {/* Meta */}
                  <div className="mt-3">
                    <p className="text-xs text-[var(--text-secondary)] truncate font-medium">{book.author}</p>
                    <div className="flex items-center gap-2 mt-1">
                      <div className={`w-2 h-2 rounded-full ${book.available ? 'bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.6)]' : 'bg-rose-500'}`} />
                      <span className="text-[10px] text-[var(--text-muted)]">{book.available ? "Available" : "Checked Out"}</span>
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
