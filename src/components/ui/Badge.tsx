import React from "react";
import { cn } from "@/lib/utils";

export interface BadgeProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: "default" | "success" | "warning" | "danger" | "info";
}

export function Badge({ children, className, variant = "default", ...props }: BadgeProps) {
  const variantClass = variant !== "default" ? `badge-${variant}` : "bg-[var(--bg-glass)] text-[var(--text-secondary)] border border-[var(--border-subtle)]";
  
  return (
    <div className={cn("badge", variantClass, className)} {...props}>
      {children}
    </div>
  );
}
