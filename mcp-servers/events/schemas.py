"""Pydantic models for the Events MCP Server."""

from pydantic import BaseModel, Field
from typing import Optional, List, Any
from enum import Enum


class EventCategory(str, Enum):
    TECH = "Tech"
    CULTURAL = "Cultural"
    SPORTS = "Sports"
    ACADEMIC = "Academic"
    WORKSHOP = "Workshop"
    HACKATHON = "Hackathon"
    SEMINAR = "Seminar"
    SOCIAL = "Social"


class EventStatus(str, Enum):
    UPCOMING = "Upcoming"
    ONGOING = "Ongoing"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Event(BaseModel):
    id: str
    title: str
    description: str
    category: EventCategory
    date: str  # ISO date string
    start_time: str
    end_time: str
    venue: str
    organizer: str
    club: Optional[str] = None
    registration_link: Optional[str] = None
    max_participants: Optional[int] = None
    current_participants: int = 0
    status: EventStatus = EventStatus.UPCOMING
    tags: List[str] = []
    contact_email: Optional[str] = None
    is_free: bool = True
    fee: Optional[float] = None


class Club(BaseModel):
    id: str
    name: str
    description: str
    category: str
    president: str
    email: str
    member_count: int
    meeting_schedule: Optional[str] = None
    social_links: dict = {}


# ─── MCP Protocol Schemas ───────────────────────────────────────────────────────

class MCPToolSchema(BaseModel):
    name: str = Field(..., description="Unique tool identifier")
    description: str = Field(..., description="Human-readable tool description")
    parameters: dict = Field(..., description="JSON Schema for tool parameters")


class ToolExecutionRequest(BaseModel):
    tool: str = Field(..., description="Name of the tool to execute")
    parameters: dict = Field(default_factory=dict, description="Tool parameters")


class ToolExecutionResponse(BaseModel):
    success: bool
    result: Optional[Any] = None
    error: Optional[str] = None
    server: str = "events"
