"""Tool definitions for the Academics MCP Server."""

from typing import Any, Callable
from dataclasses import dataclass
from schemas import MCPToolSchema
from data import (
    get_class_schedule,
    get_course_syllabus,
    search_faculty,
    get_exam_schedule,
    get_academic_calendar,
    get_all_courses,
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
    name="get_class_schedule",
    description="Get the class schedule/timetable for the CSE department. Can filter by specific day of the week. Returns course codes, rooms, timings, and instructor names.",
    parameters={
        "type": "object",
        "properties": {
            "day": {
                "type": "string",
                "description": "Filter by day of the week. If not specified, returns the full week schedule.",
                "enum": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            },
            "department": {
                "type": "string",
                "description": "Department name (default: CSE)",
                "default": "CSE"
            }
        },
        "required": []
    }
)
def tool_get_class_schedule(day: str | None = None, department: str | None = None) -> dict:
    schedule = get_class_schedule(department=department, day=day)
    return {
        "day_filter": day,
        "department": department or "CSE",
        "total_sessions": len(schedule),
        "schedule": schedule,
    }


@register_tool(
    name="get_syllabus",
    description="Get the complete syllabus for a specific course — topics covered, prerequisites, textbooks, instructor, and credits.",
    parameters={
        "type": "object",
        "properties": {
            "course_code": {
                "type": "string",
                "description": "Course code (e.g., 'CS201', 'MA201') or course name (e.g., 'Data Structures')"
            }
        },
        "required": ["course_code"]
    }
)
def tool_get_syllabus(course_code: str) -> dict:
    course = get_course_syllabus(course_code)
    if course is None:
        return {"found": False, "message": f"Course '{course_code}' not found. Try using the course code (e.g., CS201) or a keyword from the course name."}
    return {"found": True, **course}


@register_tool(
    name="search_faculty",
    description="Search the faculty directory by name, department, or research specialization. Returns office location, email, office hours, and specialization areas.",
    parameters={
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Faculty name or specialization keyword to search for"
            },
            "department": {
                "type": "string",
                "description": "Filter by department",
                "enum": [
                    "Computer Science and Engineering", "Electronics and Communication Engineering",
                    "Mechanical Engineering", "Electrical Engineering", "Mathematics", "Physics"
                ]
            }
        },
        "required": []
    }
)
def tool_search_faculty(name: str | None = None, department: str | None = None) -> dict:
    faculty = search_faculty(name, department)
    return {
        "search_name": name,
        "search_department": department,
        "total": len(faculty),
        "faculty": faculty,
    }


@register_tool(
    name="get_exam_schedule",
    description="Get upcoming exam dates and venues — mid-semester and end-semester exams. Can filter by exam type.",
    parameters={
        "type": "object",
        "properties": {
            "exam_type": {
                "type": "string",
                "description": "Filter by exam type",
                "enum": ["Mid-Semester", "End-Semester", "Quiz"]
            },
            "department": {
                "type": "string",
                "description": "Filter by department (default: CSE)"
            }
        },
        "required": []
    }
)
def tool_get_exam_schedule(exam_type: str | None = None, department: str | None = None) -> dict:
    exams = get_exam_schedule(department, exam_type)
    return {
        "type_filter": exam_type,
        "total": len(exams),
        "exams": exams,
    }


@register_tool(
    name="get_academic_calendar",
    description="Get the academic calendar — semester dates, holidays, registration deadlines, and exam periods. Can filter by month.",
    parameters={
        "type": "object",
        "properties": {
            "month": {
                "type": "integer",
                "description": "Filter by month number (1-12). If not specified, returns the full academic calendar.",
                "minimum": 1,
                "maximum": 12
            }
        },
        "required": []
    }
)
def tool_get_academic_calendar(month: int | None = None) -> dict:
    events = get_academic_calendar(month)
    return {
        "month_filter": month,
        "total": len(events),
        "events": events,
    }


@register_tool(
    name="get_all_courses",
    description="Get a list of all available courses with their codes, names, credits, and instructors.",
    parameters={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def tool_get_all_courses() -> dict:
    courses = get_all_courses()
    return {
        "total": len(courses),
        "courses": courses,
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
