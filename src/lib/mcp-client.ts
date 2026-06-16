/* ─── MCP Client ─────────────────────────────────────────────────────────────
 * HTTP client for communicating with MCP servers.
 * Handles tool discovery, tool execution, and health checks.
 * Implements caching for tool schemas to avoid redundant network calls.
 * ──────────────────────────────────────────────────────────────────────────── */

import {
  MCPToolSchema,
  MCPToolsResponse,
  MCPExecuteResponse,
  MCPHealthResponse,
  MCPServerConfig,
  MCP_SERVERS,
  ServerStatus,
} from "./types";

// ─── Schema Cache ───────────────────────────────────────────────────────────

interface CachedTools {
  tools: MCPToolSchema[];
  server: string;
  fetchedAt: number;
}

const CACHE_TTL_MS = 5 * 60 * 1000; // 5 minutes
const toolsCache: Map<string, CachedTools> = new Map();

// ─── Core Functions ─────────────────────────────────────────────────────────

/**
 * Check health status of an MCP server.
 */
export async function checkServerHealth(
  server: MCPServerConfig
): Promise<ServerStatus> {
  try {
    const response = await fetch(`${server.url}/health`, {
      signal: AbortSignal.timeout(3000),
    });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data: MCPHealthResponse = await response.json();
    return {
      name: server.name,
      displayName: server.displayName,
      emoji: server.emoji,
      healthy: data.status === "healthy",
      toolsCount: data.tools_count,
    };
  } catch (error) {
    return {
      name: server.name,
      displayName: server.displayName,
      emoji: server.emoji,
      healthy: false,
      toolsCount: 0,
      error: error instanceof Error ? error.message : "Unknown error",
    };
  }
}

/**
 * Check health of all MCP servers in parallel.
 */
export async function checkAllServersHealth(): Promise<ServerStatus[]> {
  return Promise.all(MCP_SERVERS.map(checkServerHealth));
}

/**
 * Discover available tools from an MCP server.
 * Results are cached with a TTL to reduce network overhead.
 */
export async function discoverTools(
  server: MCPServerConfig
): Promise<MCPToolSchema[]> {
  // Check cache
  const cached = toolsCache.get(server.name);
  if (cached && Date.now() - cached.fetchedAt < CACHE_TTL_MS) {
    return cached.tools;
  }

  try {
    const response = await fetch(`${server.url}/mcp/tools`, {
      signal: AbortSignal.timeout(5000),
    });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data: MCPToolsResponse = await response.json();

    // Update cache
    toolsCache.set(server.name, {
      tools: data.tools,
      server: server.name,
      fetchedAt: Date.now(),
    });

    return data.tools;
  } catch (error) {
    console.error(`Failed to discover tools from ${server.name}:`, error);
    return [];
  }
}

/**
 * Discover tools from ALL MCP servers in parallel.
 * Returns a map of server name → tools with server info attached.
 */
export async function discoverAllTools(): Promise<
  Map<string, { server: MCPServerConfig; tools: MCPToolSchema[] }>
> {
  const results = new Map<
    string,
    { server: MCPServerConfig; tools: MCPToolSchema[] }
  >();

  const promises = MCP_SERVERS.map(async (server) => {
    const tools = await discoverTools(server);
    results.set(server.name, { server, tools });
  });

  await Promise.all(promises);
  return results;
}

/**
 * Execute a tool on a specific MCP server.
 */
export async function executeTool(
  server: MCPServerConfig,
  toolName: string,
  parameters: Record<string, unknown>
): Promise<MCPExecuteResponse> {
  try {
    const response = await fetch(`${server.url}/mcp/execute`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ tool: toolName, parameters }),
      signal: AbortSignal.timeout(10000),
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    return {
      success: false,
      result: null,
      error: error instanceof Error ? error.message : "Tool execution failed",
      server: server.name,
    };
  }
}

/**
 * Find which MCP server owns a specific tool.
 */
export function findServerForTool(
  toolName: string,
  toolsMap: Map<string, { server: MCPServerConfig; tools: MCPToolSchema[] }>
): MCPServerConfig | null {
  for (const [, { server, tools }] of toolsMap) {
    if (tools.some((t) => t.name === toolName)) {
      return server;
    }
  }
  return null;
}

/**
 * Fetch data directly from an MCP server tool (for dashboard widgets).
 */
export async function fetchWidgetData<T>(
  serverName: string,
  toolName: string,
  parameters: Record<string, unknown> = {}
): Promise<T | null> {
  const server = MCP_SERVERS.find((s) => s.name === serverName);
  if (!server) return null;

  const response = await executeTool(server, toolName, parameters);
  if (response.success) {
    return response.result as T;
  }
  console.error(`Widget data fetch failed (${serverName}/${toolName}):`, response.error);
  return null;
}
