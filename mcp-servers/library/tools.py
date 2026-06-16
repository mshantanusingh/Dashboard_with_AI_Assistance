"""Tool definitions for the Library MCP Server.

Each tool is registered with a JSON Schema for its parameters that maps
directly to LLM function-calling format (OpenAI/Gemini compatible).
"""

from typing import Any, Callable
from dataclasses import dataclass, field
from schemas import MCPToolSchema
from data import (
    search_books,
    check_availability,
    get_popular_books,
    get_library_hours,
    get_all_categories,
    get_stats,
)


@dataclass
class Tool:
    """Represents an MCP tool with its schema and handler."""
    name: str
    description: str
    parameters: dict
    handler: Callable[..., Any]

    def schema(self) -> dict:
        """Return the tool schema in MCP/LLM function-calling format."""
        return MCPToolSchema(
            name=self.name,
            description=self.description,
            parameters=self.parameters,
        ).model_dump()


# ─── Tool Registry ───────────────────────────────────────────────────────────────

TOOL_REGISTRY: dict[str, Tool] = {}


def register_tool(name: str, description: str, parameters: dict):
    """Decorator to register a function as an MCP tool."""
    def decorator(func: Callable) -> Callable:
        TOOL_REGISTRY[name] = Tool(
            name=name,
            description=description,
            parameters=parameters,
            handler=func,
        )
        return func
    return decorator


# ─── Tool Definitions ────────────────────────────────────────────────────────────

@register_tool(
    name="search_books",
    description="Search the campus library catalog by book title, author name, or keyword. Returns matching books with availability status and shelf location.",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query — can be a book title, author name, or keyword"
            },
            "category": {
                "type": "string",
                "description": "Optional: filter results by book category",
                "enum": [
                    "Computer Science", "Mathematics", "Physics",
                    "Electrical Engineering", "Mechanical Engineering",
                    "Chemistry", "Literature", "Economics", "General"
                ]
            }
        },
        "required": ["query"]
    }
)
def tool_search_books(query: str, category: str | None = None) -> dict:
    """Search books in the library catalog."""
    results = search_books(query, category)
    return {
        "query": query,
        "category_filter": category,
        "total_results": len(results),
        "books": results,
    }


@register_tool(
    name="check_availability",
    description="Check if a specific book is currently available in the campus library. Returns availability status, number of copies, and shelf location.",
    parameters={
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "description": "The title (or partial title) of the book to check"
            }
        },
        "required": ["title"]
    }
)
def tool_check_availability(title: str) -> dict:
    """Check book availability by title."""
    result = check_availability(title)
    if result is None:
        return {
            "found": False,
            "message": f"No book matching '{title}' was found in the catalog."
        }
    return {
        "found": True,
        **result,
    }


@register_tool(
    name="get_popular_books",
    description="Get the most popular/in-demand books in the campus library. Popularity is determined by checkout frequency.",
    parameters={
        "type": "object",
        "properties": {
            "limit": {
                "type": "integer",
                "description": "Maximum number of books to return (default: 5)",
                "default": 5
            },
            "student_id": {
                "type": "string",
                "description": "Optional student ID for personalized recommendations (e.g. STU-101)"
            }
        },
        "required": []
    }
)
def tool_get_popular_books(limit: int = 5, student_id: str | None = None) -> dict:
    """Get popular books."""
    books = get_popular_books(limit, student_id)
    return {
        "total": len(books),
        "popular_books": books,
    }


@register_tool(
    name="get_library_hours",
    description="Get the campus library operating hours. Can return hours for a specific day or the full weekly schedule.",
    parameters={
        "type": "object",
        "properties": {
            "day": {
                "type": "string",
                "description": "Day of the week (e.g., 'Monday', 'Tuesday'). If not specified, returns full weekly schedule.",
                "enum": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            }
        },
        "required": []
    }
)
def tool_get_library_hours(day: str | None = None) -> dict:
    """Get library operating hours."""
    hours = get_library_hours(day)
    return {
        "schedule": hours,
        "note": "Hours may vary during exam periods and holidays."
    }


@register_tool(
    name="get_library_stats",
    description="Get overall statistics about the campus library — total books, availability rates, and category breakdown.",
    parameters={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def tool_get_library_stats() -> dict:
    """Get library statistics."""
    stats = get_stats()
    categories = get_all_categories()
    return {
        **stats,
        "available_categories": categories,
    }


# ─── Tool Execution ──────────────────────────────────────────────────────────────

def execute_tool(tool_name: str, parameters: dict) -> dict:
    """Execute a registered tool by name with the given parameters.

    Returns:
        dict with 'success', 'result', and optionally 'error' keys.
    """
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
        return {
            "success": True,
            "result": result,
            "error": None,
        }
    except TypeError as e:
        return {
            "success": False,
            "error": f"Invalid parameters for tool '{tool_name}': {str(e)}",
            "result": None,
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Tool execution failed: {str(e)}",
            "result": None,
        }


def get_all_tool_schemas() -> list[dict]:
    """Return schemas for all registered tools."""
    return [tool.schema() for tool in TOOL_REGISTRY.values()]
