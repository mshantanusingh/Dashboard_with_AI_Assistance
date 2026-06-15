"""Tool definitions for the Cafeteria MCP Server."""

from typing import Any, Callable
from dataclasses import dataclass
from schemas import MCPToolSchema
from data import (
    get_todays_menu,
    get_weekly_menu,
    get_nutrition_info,
    get_mess_timings,
    get_special_menus,
)


@dataclass
class Tool:
    """Represents an MCP tool with its schema and handler."""
    name: str
    description: str
    parameters: dict
    handler: Callable[..., Any]

    def schema(self) -> dict:
        return MCPToolSchema(
            name=self.name,
            description=self.description,
            parameters=self.parameters,
        ).model_dump()


TOOL_REGISTRY: dict[str, Tool] = {}


def register_tool(name: str, description: str, parameters: dict):
    """Decorator to register a function as an MCP tool."""
    def decorator(func: Callable) -> Callable:
        TOOL_REGISTRY[name] = Tool(
            name=name, description=description,
            parameters=parameters, handler=func,
        )
        return func
    return decorator


# ─── Tool Definitions ────────────────────────────────────────────────────────────

@register_tool(
    name="get_todays_menu",
    description="Get today's cafeteria/mess menu. Can filter by meal type (Breakfast, Lunch, Snacks, Dinner). Returns dishes with dietary info.",
    parameters={
        "type": "object",
        "properties": {
            "meal": {
                "type": "string",
                "description": "Filter by meal type. If not specified, returns all meals for today.",
                "enum": ["Breakfast", "Lunch", "Snacks", "Dinner"]
            }
        },
        "required": []
    }
)
def tool_get_todays_menu(meal: str | None = None) -> dict:
    return get_todays_menu(meal)


@register_tool(
    name="get_weekly_menu",
    description="Get the full weekly cafeteria/mess menu, or the menu for a specific day of the week.",
    parameters={
        "type": "object",
        "properties": {
            "day": {
                "type": "string",
                "description": "Day of the week. If not specified, returns the full weekly schedule.",
                "enum": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            }
        },
        "required": []
    }
)
def tool_get_weekly_menu(day: str | None = None) -> dict:
    menus = get_weekly_menu(day)
    return {
        "day_filter": day,
        "total_days": len(menus),
        "menus": menus,
    }


@register_tool(
    name="get_nutrition_info",
    description="Get detailed nutritional information for a specific dish served in the campus cafeteria — calories, protein, carbs, fat, fiber, and allergen info.",
    parameters={
        "type": "object",
        "properties": {
            "dish_name": {
                "type": "string",
                "description": "Name of the dish to look up (e.g., 'Paneer Butter Masala', 'Chicken Biryani')"
            }
        },
        "required": ["dish_name"]
    }
)
def tool_get_nutrition_info(dish_name: str) -> dict:
    info = get_nutrition_info(dish_name)
    if info is None:
        return {
            "found": False,
            "message": f"Nutritional info for '{dish_name}' is not available in our database."
        }
    return {"found": True, **info}


@register_tool(
    name="get_mess_timings",
    description="Get the campus mess/cafeteria operating hours for all meals — breakfast, lunch, snacks, and dinner.",
    parameters={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def tool_get_mess_timings() -> dict:
    timings = get_mess_timings()
    return {
        "timings": timings,
        "note": "Timings may vary on weekends and holidays. Saturday & Sunday breakfast starts at 08:00."
    }


@register_tool(
    name="get_special_menu",
    description="Get upcoming special and festival menus in the campus cafeteria — Independence Day, Diwali, Founders' Day, etc.",
    parameters={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def tool_get_special_menu() -> dict:
    menus = get_special_menus()
    return {
        "total": len(menus),
        "special_menus": menus,
    }


# ─── Tool Execution ──────────────────────────────────────────────────────────────

def execute_tool(tool_name: str, parameters: dict) -> dict:
    """Execute a registered tool by name with given parameters."""
    tool = TOOL_REGISTRY.get(tool_name)
    if not tool:
        available = list(TOOL_REGISTRY.keys())
        return {
            "success": False,
            "error": f"Tool '{tool_name}' not found. Available tools: {available}",
            "result": None,
        }
    try:
        result = tool.handler(**parameters)
        return {"success": True, "result": result, "error": None}
    except TypeError as e:
        return {"success": False, "error": f"Invalid parameters for '{tool_name}': {str(e)}", "result": None}
    except Exception as e:
        return {"success": False, "error": f"Tool execution failed: {str(e)}", "result": None}


def get_all_tool_schemas() -> list[dict]:
    """Return schemas for all registered tools."""
    return [tool.schema() for tool in TOOL_REGISTRY.values()]
