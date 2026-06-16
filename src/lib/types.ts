/* ─── Shared TypeScript Types ──────────────────────────────────────────────── */

// ─── MCP Protocol Types ─────────────────────────────────────────────────────

export interface MCPToolSchema {
  name: string;
  description: string;
  parameters: Record<string, unknown>;
}

export interface MCPToolsResponse {
  server: string;
  version: string;
  tools: MCPToolSchema[];
}

export interface MCPExecuteRequest {
  tool: string;
  parameters: Record<string, unknown>;
}

export interface MCPExecuteResponse {
  success: boolean;
  result: unknown;
  error: string | null;
  server: string;
}

export interface MCPHealthResponse {
  status: string;
  server: string;
  version: string;
  tools_count: number;
}

// ─── MCP Server Configuration ───────────────────────────────────────────────

export interface MCPServerConfig {
  name: string;
  displayName: string;
  emoji: string;
  url: string;
  description: string;
}

export const MCP_SERVERS: MCPServerConfig[] = [
  {
    name: "library",
    displayName: "Library",
    emoji: "📚",
    url: process.env.NEXT_PUBLIC_LIBRARY_MCP_URL || "/api/library",
    description: "Campus library — book search, availability, hours",
  },
  {
    name: "cafeteria",
    displayName: "Cafeteria",
    emoji: "🍽️",
    url: process.env.NEXT_PUBLIC_CAFETERIA_MCP_URL || "/api/cafeteria",
    description: "Mess/cafeteria — menus, nutrition, timings",
  },
  {
    name: "events",
    displayName: "Events",
    emoji: "📅",
    url: process.env.NEXT_PUBLIC_EVENTS_MCP_URL || "/api/events",
    description: "Campus events, clubs, and activities",
  },
  {
    name: "academics",
    displayName: "Academics",
    emoji: "🎓",
    url: process.env.NEXT_PUBLIC_ACADEMICS_MCP_URL || "/api/academics",
    description: "Class schedule, syllabus, faculty, exams",
  },
];

// ─── Chat Types ─────────────────────────────────────────────────────────────

export interface ChatMessage {
  id: string;
  role: "user" | "assistant" | "system";
  content: string;
  timestamp: Date;
  toolCalls?: ToolCallInfo[];
}

export interface ToolCallInfo {
  server: string;
  tool: string;
  parameters: Record<string, unknown>;
  result?: unknown;
}

// ─── Dashboard Widget Types ─────────────────────────────────────────────────

export interface ServerStatus {
  name: string;
  displayName: string;
  emoji: string;
  healthy: boolean;
  toolsCount: number;
  error?: string;
}

export interface BookInfo {
  id: string;
  title: string;
  author: string;
  available: boolean;
  available_copies: number;
  total_copies: number;
  shelf_location: string;
  category: string;
}

export interface MenuItem {
  name: string;
  is_vegetarian: boolean;
  is_vegan: boolean;
  calories: number | null;
  allergens: string[];
}

export interface MealInfo {
  meal_type: string;
  start_time: string;
  end_time: string;
  items: MenuItem[];
}

export interface EventInfo {
  id: string;
  title: string;
  description: string;
  category: string;
  date: string;
  start_time: string;
  end_time: string;
  venue: string;
  organizer: string;
  status: string;
  tags: string[];
}

export interface ClassInfo {
  course_code: string;
  course_name: string;
  instructor: string;
  day: string;
  start_time: string;
  end_time: string;
  room: string;
  type: string;
}
