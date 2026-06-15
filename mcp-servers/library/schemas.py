"""Pydantic models for the Library MCP Server."""

from pydantic import BaseModel, Field
from typing import Optional, List, Any
from enum import Enum


class BookCategory(str, Enum):
    """Categories of books in the campus library."""
    COMPUTER_SCIENCE = "Computer Science"
    MATHEMATICS = "Mathematics"
    PHYSICS = "Physics"
    ELECTRICAL_ENGINEERING = "Electrical Engineering"
    MECHANICAL_ENGINEERING = "Mechanical Engineering"
    CHEMISTRY = "Chemistry"
    LITERATURE = "Literature"
    ECONOMICS = "Economics"
    GENERAL = "General"


class Book(BaseModel):
    """Represents a book in the library catalog."""
    id: str
    title: str
    author: str
    isbn: str
    category: BookCategory
    available: bool
    total_copies: int
    available_copies: int
    shelf_location: str
    edition: Optional[str] = None
    year: Optional[int] = None
    publisher: Optional[str] = None
    description: Optional[str] = None


class LibraryHours(BaseModel):
    """Library operating hours for a specific day."""
    day: str
    open_time: str
    close_time: str
    is_open: bool = True


# ─── MCP Protocol Schemas ───────────────────────────────────────────────────────

class MCPToolSchema(BaseModel):
    """Schema for MCP tool discovery — maps directly to LLM function-calling format."""
    name: str = Field(..., description="Unique tool identifier")
    description: str = Field(..., description="Human-readable description of what the tool does")
    parameters: dict = Field(..., description="JSON Schema object describing tool parameters")


class ToolExecutionRequest(BaseModel):
    """Request body for executing a tool via MCP protocol."""
    tool: str = Field(..., description="Name of the tool to execute")
    parameters: dict = Field(default_factory=dict, description="Tool parameters as key-value pairs")


class ToolExecutionResponse(BaseModel):
    """Standardized response from tool execution."""
    success: bool
    result: Optional[Any] = None
    error: Optional[str] = None
    server: str = "library"
