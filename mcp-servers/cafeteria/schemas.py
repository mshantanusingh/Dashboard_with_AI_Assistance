"""Pydantic models for the Cafeteria MCP Server."""

from pydantic import BaseModel, Field
from typing import Optional, List, Any
from enum import Enum


class MealType(str, Enum):
    BREAKFAST = "Breakfast"
    LUNCH = "Lunch"
    SNACKS = "Snacks"
    DINNER = "Dinner"


class DayOfWeek(str, Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class DishItem(BaseModel):
    """A single dish in a meal."""
    name: str
    is_vegetarian: bool = True
    is_vegan: bool = False
    calories: Optional[int] = None
    allergens: List[str] = []


class Meal(BaseModel):
    """A meal (breakfast/lunch/dinner) with its items and timing."""
    meal_type: MealType
    start_time: str
    end_time: str
    items: List[DishItem]


class DayMenu(BaseModel):
    """Full menu for a single day."""
    day: DayOfWeek
    meals: List[Meal]
    special_note: Optional[str] = None


class NutritionInfo(BaseModel):
    """Nutritional information for a dish."""
    dish_name: str
    calories: int
    protein_g: float
    carbs_g: float
    fat_g: float
    fiber_g: float
    is_vegetarian: bool
    is_vegan: bool
    allergens: List[str]


class MessTiming(BaseModel):
    """Operating timing for a meal service."""
    meal_type: MealType
    start_time: str
    end_time: str


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
    server: str = "cafeteria"
