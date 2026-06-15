"""Pydantic models for the Academics MCP Server."""

from pydantic import BaseModel, Field
from typing import Optional, List, Any
from enum import Enum


class Department(str, Enum):
    CSE = "Computer Science and Engineering"
    ECE = "Electronics and Communication Engineering"
    ME = "Mechanical Engineering"
    EE = "Electrical Engineering"
    CE = "Civil Engineering"
    MATH = "Mathematics"
    PHYSICS = "Physics"
    CHEMISTRY = "Chemistry"
    HSS = "Humanities and Social Sciences"


class ClassSession(BaseModel):
    course_code: str
    course_name: str
    instructor: str
    day: str
    start_time: str
    end_time: str
    room: str
    type: str = "Lecture"  # Lecture, Tutorial, Lab


class Course(BaseModel):
    code: str
    name: str
    department: Department
    credits: int
    instructor: str
    description: str
    prerequisites: List[str] = []
    syllabus_topics: List[str] = []
    textbooks: List[str] = []
    semester: str = "Monsoon 2026"


class Faculty(BaseModel):
    id: str
    name: str
    department: Department
    designation: str
    email: str
    office: str
    specialization: List[str]
    office_hours: Optional[str] = None
    phone: Optional[str] = None
    profile_url: Optional[str] = None


class ExamSchedule(BaseModel):
    course_code: str
    course_name: str
    date: str
    start_time: str
    end_time: str
    venue: str
    type: str = "Mid-Semester"  # Mid-Semester, End-Semester, Quiz


class AcademicCalendarEvent(BaseModel):
    date: str
    event: str
    type: str  # Holiday, Exam, Registration, Deadline


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
    server: str = "academics"
