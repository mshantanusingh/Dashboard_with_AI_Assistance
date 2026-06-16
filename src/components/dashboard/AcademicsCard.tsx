"use client";

import { useMCPData } from "@/hooks/useMCPData";
import { usePersona } from "@/context/PersonaContext";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Skeleton } from "@/components/ui/Skeleton";
import { GraduationCap, MapPin, Clock } from "lucide-react";
import { ClassInfo } from "@/lib/types";

export function AcademicsCard() {
  const { activePersona } = usePersona();
  const currentDay = new Date().toLocaleDateString('en-US', { weekday: 'long' });
  const { data, loading, error } = useMCPData<{ schedule: ClassInfo[] }>({
    server: "academics",
    tool: "get_class_schedule",
    parameters: { day: currentDay, student_id: activePersona.id },
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
          <div className="relative pl-8 space-y-4 before:absolute before:inset-0 before:ml-[11px] before:-translate-x-px before:h-full before:w-0.5 before:bg-gradient-to-b before:from-neutral-700 before:via-neutral-800 before:to-transparent">
            {data.schedule.map((session, i) => {
              // Mock active state for the first item
              const isActive = i === 0;
              
              return (
                <div key={i} className="relative flex flex-col group">
                  {/* Timeline Dot */}
                  <div className={`absolute left-[-33px] top-4 w-3 h-3 rounded-full border-[3px] border-[#0A0A0A] flex items-center justify-center ${isActive ? 'bg-cyan-500 shadow-[0_0_8px_rgba(6,182,212,0.6)]' : 'bg-neutral-600'}`}>
                  </div>
                  
                  {/* Content Card */}
                  <div className={`w-full bg-white/[0.02] hover:bg-white/[0.04] transition-colors p-4 rounded-xl border ${isActive ? 'border-cyan-500/30' : 'border-white/5'} flex flex-col sm:flex-row sm:items-center justify-between gap-4`}>
                    <div>
                      <div className="flex items-center gap-2 mb-1.5">
                        <span className={`text-[10px] font-bold tracking-widest uppercase ${isActive ? 'text-cyan-400' : 'text-neutral-500'}`}>
                          {session.course_code}
                        </span>
                        <span className="px-1.5 py-0.5 bg-white/5 rounded text-[9px] uppercase tracking-wider text-neutral-400">
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
