import sys, os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "mcp-servers", "library"))
from tools import get_all_tool_schemas, execute_tool, TOOL_REGISTRY
from schemas import ToolExecutionRequest, ToolExecutionResponse

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/api/library/health")
def health_check():
    return {"status": "healthy", "server": "library", "version": "1.0.0", "tools_count": len(TOOL_REGISTRY)}

@app.get("/api/library/mcp/tools")
def discover_tools():
    return {"server": "library", "version": "1.0.0", "tools": get_all_tool_schemas()}

@app.post("/api/library/mcp/execute")
def execute_mcp_tool(request: ToolExecutionRequest):
    result = execute_tool(request.tool, request.parameters)
    return ToolExecutionResponse(success=result["success"], result=result["result"], error=result.get("error"), server="library")
