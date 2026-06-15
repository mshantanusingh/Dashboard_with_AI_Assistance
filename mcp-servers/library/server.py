"""Library MCP Server — Independent FastAPI service.

Exposes campus library data through MCP-compliant endpoints:
  - GET  /health       → Health check
  - GET  /mcp/tools    → Tool discovery (returns available tools with schemas)
  - POST /mcp/execute  → Tool execution (run a tool with parameters)

Port: 8001
"""

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import ToolExecutionRequest, ToolExecutionResponse
from tools import get_all_tool_schemas, execute_tool, TOOL_REGISTRY

# ─── Logging ──────────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("library-mcp")


# ─── Application Lifecycle ───────────────────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown events."""
    logger.info(f"📚 Library MCP Server starting — {len(TOOL_REGISTRY)} tools registered")
    for name in TOOL_REGISTRY:
        logger.info(f"  ✓ Tool registered: {name}")
    yield
    logger.info("📚 Library MCP Server shutting down")


# ─── FastAPI Application ─────────────────────────────────────────────────────────

app = FastAPI(
    title="Library MCP Server",
    description="MCP-compliant server for campus library data — book search, availability, hours, and statistics.",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS — allow frontend to call this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Health Check ─────────────────────────────────────────────────────────────────

@app.get("/health")
async def health_check():
    """Health check endpoint for service monitoring."""
    return {
        "status": "healthy",
        "server": "library",
        "version": "1.0.0",
        "tools_count": len(TOOL_REGISTRY),
    }


# ─── MCP Protocol Endpoints ──────────────────────────────────────────────────────

@app.get("/mcp/tools")
async def discover_tools():
    """MCP Tool Discovery — returns all available tools with their JSON Schema parameters.

    This response format is designed to map directly to LLM function-calling schemas,
    enabling the AI orchestrator to automatically discover and invoke tools.
    """
    tools = get_all_tool_schemas()
    return {
        "server": "library",
        "version": "1.0.0",
        "tools": tools,
    }


@app.post("/mcp/execute", response_model=ToolExecutionResponse)
async def execute_mcp_tool(request: ToolExecutionRequest):
    """MCP Tool Execution — execute a tool by name with the given parameters.

    The AI orchestrator calls this endpoint after the LLM decides which tool to invoke.
    """
    logger.info(f"Executing tool: {request.tool} with params: {request.parameters}")

    result = execute_tool(request.tool, request.parameters)

    if not result["success"]:
        logger.warning(f"Tool execution failed: {result['error']}")

    return ToolExecutionResponse(
        success=result["success"],
        result=result["result"],
        error=result["error"],
        server="library",
    )


# ─── Entry Point ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_level="info",
    )
