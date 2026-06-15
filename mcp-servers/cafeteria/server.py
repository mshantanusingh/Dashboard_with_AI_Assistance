"""Cafeteria MCP Server — Independent FastAPI service.

Exposes campus cafeteria/mess data through MCP-compliant endpoints:
  - GET  /health       → Health check
  - GET  /mcp/tools    → Tool discovery
  - POST /mcp/execute  → Tool execution

Port: 8002
"""

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import ToolExecutionRequest, ToolExecutionResponse
from tools import get_all_tool_schemas, execute_tool, TOOL_REGISTRY

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("cafeteria-mcp")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"🍽️ Cafeteria MCP Server starting — {len(TOOL_REGISTRY)} tools registered")
    for name in TOOL_REGISTRY:
        logger.info(f"  ✓ Tool registered: {name}")
    yield
    logger.info("🍽️ Cafeteria MCP Server shutting down")


app = FastAPI(
    title="Cafeteria MCP Server",
    description="MCP-compliant server for campus cafeteria data — menus, nutrition, timings.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "server": "cafeteria",
        "version": "1.0.0",
        "tools_count": len(TOOL_REGISTRY),
    }


@app.get("/mcp/tools")
async def discover_tools():
    tools = get_all_tool_schemas()
    return {"server": "cafeteria", "version": "1.0.0", "tools": tools}


@app.post("/mcp/execute", response_model=ToolExecutionResponse)
async def execute_mcp_tool(request: ToolExecutionRequest):
    logger.info(f"Executing tool: {request.tool} with params: {request.parameters}")
    result = execute_tool(request.tool, request.parameters)
    if not result["success"]:
        logger.warning(f"Tool execution failed: {result['error']}")
    return ToolExecutionResponse(
        success=result["success"],
        result=result["result"],
        error=result["error"],
        server="cafeteria",
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8002, reload=True, log_level="info")
