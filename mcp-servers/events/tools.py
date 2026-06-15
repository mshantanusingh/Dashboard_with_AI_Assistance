"""Tool definitions for the Events MCP Server."""

from typing import Any, Callable
from dataclasses import dataclass
from schemas import MCPToolSchema
from data import (
    get_upcoming_events,
    search_events,
    get_event_details,
    get_club_info,
    get_events_by_club,
)


@dataclass
class Tool:
    name: str
    description: str
    parameters: dict
    handler: Callable[..., Any]

    def schema(self) -> dict:
        return MCPToolSchema(
            name=self.name, description=self.description, parameters=self.parameters,
        ).model_dump()


TOOL_REGISTRY: dict[str, Tool] = {}


def register_tool(name: str, description: str, parameters: dict):
    def decorator(func: Callable) -> Callable:
        TOOL_REGISTRY[name] = Tool(name=name, description=description, parameters=parameters, handler=func)
        return func
    return decorator


# ─── Tool Definitions ────────────────────────────────────────────────────────────

@register_tool(
    name="get_upcoming_events",
    description="Get upcoming campus events within a specified number of days. Can filter by category (Tech, Cultural, Sports, Academic, Workshop, Hackathon, Seminar, Social).",
    parameters={
        "type": "object",
        "properties": {
            "days": {
                "type": "integer",
                "description": "Number of days to look ahead (default: 30)",
                "default": 30
            },
            "category": {
                "type": "string",
                "description": "Filter by event category",
                "enum": ["Tech", "Cultural", "Sports", "Academic", "Workshop", "Hackathon", "Seminar", "Social"]
            }
        },
        "required": []
    }
)
def tool_get_upcoming_events(days: int = 30, category: str | None = None) -> dict:
    events = get_upcoming_events(days, category)
    return {
        "days_ahead": days,
        "category_filter": category,
        "total": len(events),
        "events": events,
    }


@register_tool(
    name="search_events",
    description="Search campus events by keyword. Searches in event title, description, and tags. Returns matching events including past ones.",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search keyword (e.g., 'hackathon', 'workshop', 'cricket', 'coding')"
            }
        },
        "required": ["query"]
    }
)
def tool_search_events(query: str) -> dict:
    events = search_events(query)
    return {
        "query": query,
        "total": len(events),
        "events": events,
    }


@register_tool(
    name="get_event_details",
    description="Get full details of a specific campus event by its event ID.",
    parameters={
        "type": "object",
        "properties": {
            "event_id": {
                "type": "string",
                "description": "Event ID (e.g., 'EVT-001')"
            }
        },
        "required": ["event_id"]
    }
)
def tool_get_event_details(event_id: str) -> dict:
    event = get_event_details(event_id)
    if event is None:
        return {"found": False, "message": f"Event '{event_id}' not found."}
    return {"found": True, **event}


@register_tool(
    name="get_club_info",
    description="Get information about student clubs on campus — description, president, member count, meeting schedule, and social links. Search by club name or get all clubs.",
    parameters={
        "type": "object",
        "properties": {
            "club_name": {
                "type": "string",
                "description": "Name of the club to search for. If not specified, returns all clubs."
            }
        },
        "required": []
    }
)
def tool_get_club_info(club_name: str | None = None) -> dict:
    clubs = get_club_info(club_name)
    return {
        "search": club_name,
        "total": len(clubs),
        "clubs": clubs,
    }


@register_tool(
    name="get_club_events",
    description="Get all events organized by a specific student club.",
    parameters={
        "type": "object",
        "properties": {
            "club_name": {
                "type": "string",
                "description": "Name of the club (e.g., 'Coding Club', 'GDSC')"
            }
        },
        "required": ["club_name"]
    }
)
def tool_get_club_events(club_name: str) -> dict:
    events = get_events_by_club(club_name)
    return {
        "club": club_name,
        "total": len(events),
        "events": events,
    }


# ─── Tool Execution ──────────────────────────────────────────────────────────────

def execute_tool(tool_name: str, parameters: dict) -> dict:
    tool = TOOL_REGISTRY.get(tool_name)
    if not tool:
        return {"success": False, "error": f"Tool '{tool_name}' not found. Available: {list(TOOL_REGISTRY.keys())}", "result": None}
    try:
        result = tool.handler(**parameters)
        return {"success": True, "result": result, "error": None}
    except TypeError as e:
        return {"success": False, "error": f"Invalid parameters for '{tool_name}': {str(e)}", "result": None}
    except Exception as e:
        return {"success": False, "error": f"Tool execution failed: {str(e)}", "result": None}


def get_all_tool_schemas() -> list[dict]:
    return [tool.schema() for tool in TOOL_REGISTRY.values()]
