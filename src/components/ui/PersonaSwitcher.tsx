"use client";

import { usePersona, PERSONAS } from "@/context/PersonaContext";
import { UserCircle } from "lucide-react";

export function PersonaSwitcher() {
  const { activePersona, setActivePersona } = usePersona();

  return (
    <div className="flex items-center gap-2 bg-white/[0.03] border border-white/10 rounded-full pl-2 pr-3 py-1.5 shadow-sm">
      <UserCircle className="w-4 h-4 text-neutral-400" />
      <select
        value={activePersona.id}
        onChange={(e) => {
          const persona = PERSONAS.find((p) => p.id === e.target.value);
          if (persona) setActivePersona(persona);
        }}
        className="bg-transparent text-xs font-medium text-neutral-200 focus:outline-none appearance-none cursor-pointer"
        style={{ WebkitAppearance: "none", MozAppearance: "none" }}
      >
        {PERSONAS.map((p) => (
          <option key={p.id} value={p.id} className="bg-neutral-900 text-neutral-200">
            {p.name}
          </option>
        ))}
      </select>
      <div className="pointer-events-none text-neutral-500 text-[10px] ml-1">▼</div>
    </div>
  );
}
