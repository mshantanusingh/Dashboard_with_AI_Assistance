"use client";

import { useMCPData } from "@/hooks/useMCPData";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { Skeleton } from "@/components/ui/Skeleton";
import { Coffee, Utensils } from "lucide-react";
import { MealInfo } from "@/lib/types";

export function CafeteriaCard() {
  const { data, loading, error } = useMCPData<{ meals: MealInfo[] }>({
    server: "cafeteria",
    tool: "get_todays_menu",
    refreshInterval: 60000 * 30, // 30 mins
  });

  // Simple logic to find current or next meal
  const getCurrentMeal = () => {
    if (!data?.meals || data.meals.length === 0) return null;
    const now = new Date();
    const currentHour = now.getHours();
    
    if (currentHour < 10) return data.meals.find(m => m.meal_type === "Breakfast");
    if (currentHour < 15) return data.meals.find(m => m.meal_type === "Lunch");
    if (currentHour < 18) return data.meals.find(m => m.meal_type === "Snacks");
    return data.meals.find(m => m.meal_type === "Dinner");
  };

  const meal = getCurrentMeal() || (data?.meals ? data.meals[0] : null);

  return (
    <Card className="bento-item-wide overflow-hidden flex flex-col h-full bg-black/40 border border-[var(--border-subtle)] shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]">
      <CardHeader className="pb-3 border-b border-white/5 bg-gradient-to-b from-white/5 to-transparent">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-[var(--accent-amber)]/10 rounded-lg">
              <Utensils className="w-5 h-5 text-[var(--accent-amber)]" />
            </div>
            <div>
              <CardTitle className="text-lg">Campus Dining</CardTitle>
              <CardDescription className="text-xs uppercase tracking-wider text-[var(--text-muted)]">Live Menu</CardDescription>
            </div>
          </div>
          {meal && (
            <div className="px-3 py-1 bg-amber-500/10 border border-amber-500/20 rounded-full text-amber-500 text-xs font-bold tracking-widest uppercase">
              {meal.meal_type}
            </div>
          )}
        </div>
      </CardHeader>
      <CardContent className="flex-1 p-5 relative">
        {loading ? (
          <div className="flex flex-wrap gap-2">
            <Skeleton className="h-8 w-24 rounded-full" />
            <Skeleton className="h-8 w-32 rounded-full" />
            <Skeleton className="h-8 w-28 rounded-full" />
            <Skeleton className="h-8 w-20 rounded-full" />
          </div>
        ) : error ? (
          <div className="text-sm text-[var(--accent-rose)]">Failed to load menu</div>
        ) : meal ? (
          <div className="flex flex-col h-full justify-between">
            <div>
              <div className="text-[10px] text-[var(--text-muted)] font-mono uppercase tracking-widest mb-4 flex items-center gap-2">
                <span className="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-pulse" />
                Served {meal.start_time} — {meal.end_time}
              </div>
              <div className="flex flex-wrap gap-2">
                {meal.items.map((item, i) => (
                  <div key={i} className="flex items-center gap-2 bg-white/5 hover:bg-white/10 transition-colors px-3 py-1.5 rounded-full border border-white/10 shadow-sm cursor-default">
                    {item.is_vegetarian ? (
                      <span className="text-[10px] text-emerald-400">🥬</span>
                    ) : (
                      <span className="text-[10px] text-rose-400">🥩</span>
                    )}
                    <span className="text-sm font-medium text-white/90">{item.name}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        ) : (
          <div className="text-sm text-[var(--text-muted)]">Menu unavailable</div>
        )}
      </CardContent>
    </Card>
  );
}
