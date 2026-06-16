"use client";

import { useMCPData } from "@/hooks/useMCPData";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Skeleton } from "@/components/ui/Skeleton";
import { GraduationCap, MapPin, Clock } from "lucide-react";
import { ClassInfo } from "@/lib/types";

export function AcademicsCard() {
  const currentDay = new Date().toLocaleDateString('en-US', { weekday: 'long' });
  const { data, loading, error } = useMCPData<{ schedule: ClassInfo[] }>({
    server: "academics",
    tool: "get_class_schedule",
    parameters: { day: currentDay },
  });

  return (
    <Card className="bento-item-wide overflow-hidden flex flex-col h-full bg-black/40 border border-[var(--border-subtle)] shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]">
      <CardHeader className="pb-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-[var(--accent-cyan)]/10 rounded-lg">
              <GraduationCap className="w-5 h-5 text-[var(--accent-cyan)]" />
            </div>
            <div>
              <CardTitle className="text-lg">Class Schedule</CardTitle>
              <CardDescription className="text-xs uppercase tracking-wider text-[var(--text-muted)]">Live Timeline</CardDescription>
            </div>
          </div>
          <div className="px-3 py-1 bg-white/5 border border-white/10 rounded-full text-white/80 text-xs font-bold tracking-widest uppercase">
            {currentDay}
          </div>
        </div>
      </CardHeader>
      <CardContent className="flex-1 overflow-y-auto no-scrollbar relative p-6 pt-2">
        {loading ? (
          <div className="space-y-6">
            <Skeleton className="h-16 w-full rounded-xl" />
            <Skeleton className="h-16 w-full rounded-xl" />
          </div>
        ) : error ? (
          <div className="text-sm text-[var(--accent-rose)]">Failed to load schedule</div>
        ) : data?.schedule && data.schedule.length > 0 ? (
          <div className="relative pl-6 space-y-6 before:absolute before:inset-0 before:ml-[7px] before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-[var(--accent-cyan)] before:via-white/10 before:to-transparent">
            {data.schedule.map((session, i) => {
              // Mock active state for the first item
              const isActive = i === 0;
              
              return (
                <div key={i} className="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group">
                  {/* Timeline Dot */}
                  <div className={`absolute left-[-29px] w-4 h-4 rounded-full border-2 border-black flex items-center justify-center ${isActive ? 'bg-[var(--accent-cyan)] timeline-dot' : 'bg-white/20'}`}>
                  </div>
                  
                  {/* Content Card */}
                  <div className={`w-full bg-white/5 hover:bg-white/10 transition-colors p-4 rounded-xl border ${isActive ? 'border-[var(--accent-cyan)]/30 shadow-[0_0_15px_rgba(6,182,212,0.15)]' : 'border-white/5'} flex flex-col sm:flex-row sm:items-center justify-between gap-4`}>
                    <div>
                      <div className="flex items-center gap-2 mb-1">
                        <span className={`text-[10px] font-bold tracking-widest uppercase ${isActive ? 'text-[var(--accent-cyan)]' : 'text-white/50'}`}>
                          {session.course_code}
                        </span>
                        <span className="px-1.5 py-0.5 bg-white/10 rounded text-[9px] uppercase tracking-wider text-white/70">
                          {session.type}
                        </span>
                      </div>
                      <h4 className="text-sm font-semibold text-white/90">{session.course_name}</h4>
                    </div>
                    
                    <div className="flex sm:flex-col items-center sm:items-end gap-3 sm:gap-1 text-xs text-[var(--text-muted)] font-medium">
                      <div className="flex items-center gap-1.5">
                        <Clock className="w-3.5 h-3.5" /> 
                        <span>{session.start_time} — {session.end_time}</span>
                      </div>
                      <div className="flex items-center gap-1.5">
                        <MapPin className="w-3.5 h-3.5" />
                        <span>{session.room}</span>
                      </div>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        ) : (
          <div className="h-full flex items-center justify-center text-sm text-[var(--text-muted)] flex-col gap-2">
            <span className="text-2xl opacity-50">🎉</span> 
            <span>No classes scheduled for today!</span>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
