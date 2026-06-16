"use client";

import { useMCPData } from "@/hooks/useMCPData";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Skeleton } from "@/components/ui/Skeleton";
import { CalendarDays, MapPin, Clock } from "lucide-react";
import { EventInfo } from "@/lib/types";

export function EventsCard() {
  const { data, loading, error } = useMCPData<{ events: EventInfo[] }>({
    server: "events",
    tool: "get_upcoming_events",
    parameters: { days: 7 },
  });

  const upcomingEvents = data?.events?.slice(0, 3) || [];

  return (
    <Card className="bento-item-tall overflow-hidden flex flex-col h-full bg-black/40 border border-[var(--border-subtle)] shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]">
      <CardHeader className="pb-4">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-[var(--accent-emerald)]/10 rounded-lg">
            <CalendarDays className="w-5 h-5 text-[var(--accent-emerald)]" />
          </div>
          <div>
            <CardTitle className="text-lg">Campus Events</CardTitle>
            <CardDescription className="text-xs uppercase tracking-wider text-[var(--text-muted)]">Upcoming This Week</CardDescription>
          </div>
        </div>
      </CardHeader>
      <CardContent className="flex-1 overflow-y-auto no-scrollbar p-6 pt-2 flex flex-col gap-4">
        {loading ? (
          Array(3).fill(0).map((_, i) => (
            <div key={i} className="flex gap-4">
              <Skeleton className="h-14 w-12 rounded-lg" />
              <div className="flex flex-col gap-2 flex-1">
                <Skeleton className="h-4 w-3/4" />
                <Skeleton className="h-3 w-1/2" />
              </div>
            </div>
          ))
        ) : error ? (
          <div className="text-sm text-[var(--accent-rose)]">Failed to load events</div>
        ) : upcomingEvents.length > 0 ? (
          upcomingEvents.map((event) => {
            // Parse date to extract day number and short month
            const dateObj = new Date(event.date);
            const dayNum = dateObj.getDate() || event.date.split('-')[2];
            const month = dateObj.toLocaleString('en-us', { month: 'short' }) || "MMM";
            
            return (
              <div key={event.id} className="group flex gap-4 p-3 -mx-3 rounded-xl hover:bg-white/[0.02] transition-colors cursor-pointer border border-transparent hover:border-white/5">
                {/* Date Block */}
                <div className="flex flex-col items-center justify-center min-w-12 h-14 bg-white/[0.03] border border-white/5 rounded-lg transition-colors group-hover:bg-white/[0.06] group-hover:border-white/10">
                  <span className="text-[10px] font-bold uppercase tracking-widest text-neutral-400">{month}</span>
                  <span className="text-lg font-medium leading-none text-neutral-200 mt-0.5">{dayNum}</span>
                </div>
                
                {/* Details */}
                <div className="flex flex-col justify-center min-w-0 flex-1">
                  <h4 className="text-sm font-medium text-neutral-200 truncate group-hover:text-white transition-colors mb-1.5">
                    {event.title}
                  </h4>
                  <div className="flex flex-col gap-0.5 text-[11px] text-[var(--text-muted)]">
                    <div className="flex items-center gap-1.5">
                      <Clock className="w-3 h-3" /> {event.start_time}
                    </div>
                    <div className="flex items-center gap-1.5 truncate">
                      <MapPin className="w-3 h-3 shrink-0" /> <span className="truncate">{event.venue}</span>
                    </div>
                  </div>
                </div>
              </div>
            );
          })
        ) : (
          <div className="text-sm text-[var(--text-muted)] flex flex-col items-center justify-center h-full gap-3">
            <div className="w-12 h-12 rounded-full border border-dashed border-white/20 flex items-center justify-center">
              <CalendarDays className="w-5 h-5 opacity-40" />
            </div>
            <span>No upcoming events</span>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
