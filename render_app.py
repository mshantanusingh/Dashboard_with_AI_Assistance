from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

# Import all individual FastAPI apps from our Vercel API routes
from api.academics import app as academics_app
from api.library import app as library_app
from api.cafeteria import app as cafeteria_app
from api.events import app as events_app

app = FastAPI(title="CampusAI MCP Servers - Unified Backend")

# Add permissive CORS for the frontend to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, change this to your Vercel frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Merge all routes into a single FastAPI app
# This allows us to run them all via a single Uvicorn instance on Render/Railway
# while keeping them separate for Vercel Serverless Functions.
for route in academics_app.routes:
    app.routes.append(route)

for route in library_app.routes:
    app.routes.append(route)

for route in cafeteria_app.routes:
    app.routes.append(route)

for route in events_app.routes:
    app.routes.append(route)

@app.get("/")
def read_root():
    return {
        "message": "CampusAI Unified Backend is running",
        "endpoints": [
            "/api/academics/mcp/tools",
            "/api/library/mcp/tools",
            "/api/cafeteria/mcp/tools",
            "/api/events/mcp/tools"
        ]
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("render_app:app", host="0.0.0.0", port=port)
