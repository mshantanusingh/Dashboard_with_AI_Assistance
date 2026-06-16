"""Events MCP Server — Independent FastAPI service.

Port: 8003
"""

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import ToolExecutionRequest, ToolExecutionResponse
from tools import get_all_tool_schemas, execute_tool, TOOL_REGISTRY

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("events-mcp")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"📅 Events MCP Server starting — {len(TOOL_REGISTRY)} tools registered")
    for name in TOOL_REGISTRY:
        logger.info(f"  ✓ Tool registered: {name}")
    yield
    logger.info("📅 Events MCP Server shutting down")


app = FastAPI(
    title="Events MCP Server",
    description="MCP-compliant server for campus events, clubs, and activities.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/health")
async def health_check():
    return {"status": "healthy", "server": "events", "version": "1.0.0", "tools_count": len(TOOL_REGISTRY)}


@app.get("/mcp/tools")
async def discover_tools():
    return {"server": "events", "version": "1.0.0", "tools": get_all_tool_schemas()}


@app.post("/mcp/execute", response_model=ToolExecutionResponse)
async def execute_mcp_tool(request: ToolExecutionRequest):
    logger.info(f"Executing tool: {request.tool} with params: {request.parameters}")
    result = execute_tool(request.tool, request.parameters)
    if not result["success"]:
        logger.warning(f"Tool execution failed: {result['error']}")
    return ToolExecutionResponse(success=result["success"], result=result["result"], error=result["error"], server="events")


if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8003))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True, log_level="info")
