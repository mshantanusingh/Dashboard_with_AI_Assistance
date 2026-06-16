"use client";

import { useState, useEffect } from "react";
import { checkAllServersHealth } from "@/lib/mcp-client";
import { ServerStatus } from "@/lib/types";

export function ServerStatusDisplay() {
  const [statuses, setStatuses] = useState<ServerStatus[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function checkHealth() {
      try {
        const results = await checkAllServersHealth();
        setStatuses(results);
      } catch (e) {
        console.error("Health check failed:", e);
      } finally {
        setLoading(false);
      }
    }

    checkHealth();
    // Re-check every minute
    const interval = setInterval(checkHealth, 60000);
    return () => clearInterval(interval);
  }, []);

  if (loading && statuses.length === 0) {
    return <div className="text-sm text-[var(--text-muted)] animate-pulse">Checking MCP servers...</div>;
  }

  const allHealthy = statuses.every((s) => s.healthy);
  const onlineCount = statuses.filter((s) => s.healthy).length;

  return (
    <div className="flex items-center gap-3 bg-[var(--bg-card)] px-3 py-1.5 rounded-full border border-[var(--border-subtle)] text-xs">
      <div className="flex items-center gap-1.5">
        <span className={`status-dot ${allHealthy ? 'online' : 'offline'}`}></span>
        <span className="font-medium">{onlineCount}/{statuses.length} MCP Servers</span>
      </div>
      
      <div className="flex gap-1 border-l border-[var(--border-subtle)] pl-3">
        {statuses.map((server) => (
          <div 
            key={server.name}
            className="relative group cursor-help"
            title={`${server.displayName}: ${server.healthy ? 'Online (' + server.toolsCount + ' tools)' : 'Offline'}`}
          >
            <span className={`opacity-${server.healthy ? '100' : '40 grayscale'}`}>
              {server.emoji}
            </span>
            {!server.healthy && (
              <div className="absolute -bottom-1 -right-1 w-2 h-2 bg-rose-500 rounded-full border border-[var(--bg-card)]" />
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
