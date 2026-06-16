"use client";

import React, { createContext, useContext, useState, ReactNode } from "react";

export type Persona = {
  id: string;
  name: string;
  role: string;
  department: string;
  year: string;
};

export const PERSONAS: Persona[] = [
  {
    id: "STU-101",
    name: "Alex (Freshman CS)",
    role: "Student",
    department: "Computer Science",
    year: "Freshman",
  },
  {
    id: "STU-404",
    name: "Jordan (Senior Math)",
    role: "Student",
    department: "Mathematics",
    year: "Senior",
  },
];

interface PersonaContextType {
  activePersona: Persona;
  setActivePersona: (persona: Persona) => void;
}

const PersonaContext = createContext<PersonaContextType | undefined>(undefined);

export function PersonaProvider({ children }: { children: ReactNode }) {
  const [activePersona, setActivePersona] = useState<Persona>(PERSONAS[0]);

  return (
    <PersonaContext.Provider value={{ activePersona, setActivePersona }}>
      {children}
    </PersonaContext.Provider>
  );
}

export function usePersona() {
  const context = useContext(PersonaContext);
  if (context === undefined) {
    throw new Error("usePersona must be used within a PersonaProvider");
  }
  return context;
}
