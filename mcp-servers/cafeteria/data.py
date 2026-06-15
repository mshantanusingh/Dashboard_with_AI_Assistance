"""Mock data store for the Cafeteria MCP Server.

Realistic Indian campus mess menu data. In production, this would
connect to the mess management system or a regularly updated database.
"""

from schemas import (
    DayMenu, Meal, MealType, DayOfWeek, DishItem,
    NutritionInfo, MessTiming,
)


# ─── Mess Timings ────────────────────────────────────────────────────────────────

MESS_TIMINGS: list[MessTiming] = [
    MessTiming(meal_type=MealType.BREAKFAST, start_time="07:30", end_time="09:30"),
    MessTiming(meal_type=MealType.LUNCH, start_time="12:00", end_time="14:00"),
    MessTiming(meal_type=MealType.SNACKS, start_time="17:00", end_time="18:00"),
    MessTiming(meal_type=MealType.DINNER, start_time="19:30", end_time="21:30"),
]


# ─── Weekly Menu ─────────────────────────────────────────────────────────────────

WEEKLY_MENU: list[DayMenu] = [
    DayMenu(
        day=DayOfWeek.MONDAY,
        meals=[
            Meal(
                meal_type=MealType.BREAKFAST,
                start_time="07:30",
                end_time="09:30",
                items=[
                    DishItem(name="Aloo Paratha", is_vegetarian=True, calories=300, allergens=["gluten"]),
                    DishItem(name="Curd", is_vegetarian=True, calories=60, allergens=["dairy"]),
                    DishItem(name="Butter", is_vegetarian=True, calories=100, allergens=["dairy"]),
                    DishItem(name="Tea/Coffee", is_vegetarian=True, is_vegan=True, calories=30),
                    DishItem(name="Bread & Jam", is_vegetarian=True, calories=180, allergens=["gluten"]),
                    DishItem(name="Boiled Eggs", is_vegetarian=False, calories=155),
                    DishItem(name="Banana", is_vegetarian=True, is_vegan=True, calories=89),
                ],
            ),
            Meal(
                meal_type=MealType.LUNCH,
                start_time="12:00",
                end_time="14:00",
                items=[
                    DishItem(name="Rice", is_vegetarian=True, is_vegan=True, calories=200),
                    DishItem(name="Dal Tadka", is_vegetarian=True, is_vegan=True, calories=150),
                    DishItem(name="Paneer Butter Masala", is_vegetarian=True, calories=280, allergens=["dairy"]),
                    DishItem(name="Chapati", is_vegetarian=True, is_vegan=True, calories=120, allergens=["gluten"]),
                    DishItem(name="Mixed Raita", is_vegetarian=True, calories=70, allergens=["dairy"]),
                    DishItem(name="Green Salad", is_vegetarian=True, is_vegan=True, calories=30),
                    DishItem(name="Pickle", is_vegetarian=True, is_vegan=True, calories=10),
                ],
            ),
            Meal(
                meal_type=MealType.SNACKS,
                start_time="17:00",
                end_time="18:00",
                items=[
                    DishItem(name="Samosa", is_vegetarian=True, calories=250, allergens=["gluten"]),
                    DishItem(name="Tea", is_vegetarian=True, calories=30, allergens=["dairy"]),
                ],
            ),
            Meal(
                meal_type=MealType.DINNER,
                start_time="19:30",
                end_time="21:30",
                items=[
                    DishItem(name="Rice", is_vegetarian=True, is_vegan=True, calories=200),
                    DishItem(name="Dal Makhani", is_vegetarian=True, calories=200, allergens=["dairy"]),
                    DishItem(name="Chicken Curry", is_vegetarian=False, calories=350),
                    DishItem(name="Chapati", is_vegetarian=True, is_vegan=True, calories=120, allergens=["gluten"]),
                    DishItem(name="Gulab Jamun", is_vegetarian=True, calories=175, allergens=["dairy", "gluten"]),
                    DishItem(name="Green Salad", is_vegetarian=True, is_vegan=True, calories=30),
                ],
            ),
        ],
    ),
    DayMenu(
        day=DayOfWeek.TUESDAY,
        meals=[
            Meal(
                meal_type=MealType.BREAKFAST,
                start_time="07:30",
                end_time="09:30",
                items=[
                    DishItem(name="Poha", is_vegetarian=True, is_vegan=True, calories=250),
                    DishItem(name="Upma", is_vegetarian=True, calories=200, allergens=["gluten"]),
                    DishItem(name="Tea/Coffee", is_vegetarian=True, calories=30),
                    DishItem(name="Bread & Butter", is_vegetarian=True, calories=200, allergens=["gluten", "dairy"]),
                    DishItem(name="Boiled Eggs", is_vegetarian=False, calories=155),
                    DishItem(name="Milk", is_vegetarian=True, calories=120, allergens=["dairy"]),
                ],
            ),
            Meal(
                meal_type=MealType.LUNCH,
                start_time="12:00",
                end_time="14:00",
                items=[
                    DishItem(name="Jeera Rice", is_vegetarian=True, is_vegan=True, calories=220),
                    DishItem(name="Arhar Dal", is_vegetarian=True, is_vegan=True, calories=140),
                    DishItem(name="Chole Masala", is_vegetarian=True, is_vegan=True, calories=200),
                    DishItem(name="Chapati", is_vegetarian=True, is_vegan=True, calories=120, allergens=["gluten"]),
                    DishItem(name="Boondi Raita", is_vegetarian=True, calories=80, allergens=["dairy"]),
                    DishItem(name="Salad", is_vegetarian=True, is_vegan=True, calories=30),
                ],
            ),
            Meal(
                meal_type=MealType.SNACKS,
                start_time="17:00",
                end_time="18:00",
                items=[
                    DishItem(name="Bread Pakora", is_vegetarian=True, calories=220, allergens=["gluten"]),
                    DishItem(name="Tea", is_vegetarian=True, calories=30, allergens=["dairy"]),
                ],
            ),
            Meal(
                meal_type=MealType.DINNER,
                start_time="19:30",
                end_time="21:30",
                items=[
                    DishItem(name="Rice", is_vegetarian=True, is_vegan=True, calories=200),
                    DishItem(name="Moong Dal", is_vegetarian=True, is_vegan=True, calories=130),
                    DishItem(name="Egg Curry", is_vegetarian=False, calories=280),
                    DishItem(name="Aloo Gobi", is_vegetarian=True, is_vegan=True, calories=180),
                    DishItem(name="Chapati", is_vegetarian=True, is_vegan=True, calories=120, allergens=["gluten"]),
                    DishItem(name="Ice Cream", is_vegetarian=True, calories=200, allergens=["dairy"]),
                ],
            ),
        ],
    ),
    DayMenu(
        day=DayOfWeek.WEDNESDAY,
        meals=[
            Meal(
                meal_type=MealType.BREAKFAST,
                start_time="07:30",
                end_time="09:30",
                items=[
                    DishItem(name="Idli Sambhar", is_vegetarian=True, is_vegan=True, calories=230),
                    DishItem(name="Coconut Chutney", is_vegetarian=True, is_vegan=True, calories=50),
                    DishItem(name="Tea/Coffee", is_vegetarian=True, calories=30),
                    DishItem(name="Bread & Jam", is_vegetarian=True, calories=180, allergens=["gluten"]),
                    DishItem(name="Banana", is_vegetarian=True, is_vegan=True, calories=89),
                ],
            ),
            Meal(
                meal_type=MealType.LUNCH,
                start_time="12:00",
                end_time="14:00",
                items=[
                    DishItem(name="Rice", is_vegetarian=True, is_vegan=True, calories=200),
                    DishItem(name="Masoor Dal", is_vegetarian=True, is_vegan=True, calories=145),
                    DishItem(name="Kadai Paneer", is_vegetarian=True, calories=290, allergens=["dairy"]),
                    DishItem(name="Chapati", is_vegetarian=True, is_vegan=True, calories=120, allergens=["gluten"]),
                    DishItem(name="Papad", is_vegetarian=True, is_vegan=True, calories=40),
                    DishItem(name="Salad", is_vegetarian=True, is_vegan=True, calories=30),
                ],
            ),
            Meal(
                meal_type=MealType.SNACKS,
                start_time="17:00",
                end_time="18:00",
                items=[
                    DishItem(name="Vada Pav", is_vegetarian=True, calories=290, allergens=["gluten"]),
                    DishItem(name="Tea", is_vegetarian=True, calories=30, allergens=["dairy"]),
                ],
            ),
            Meal(
                meal_type=MealType.DINNER,
                start_time="19:30",
                end_time="21:30",
                items=[
                    DishItem(name="Veg Biryani", is_vegetarian=True, calories=350),
                    DishItem(name="Chicken Biryani", is_vegetarian=False, calories=450),
                    DishItem(name="Raita", is_vegetarian=True, calories=70, allergens=["dairy"]),
                    DishItem(name="Salan", is_vegetarian=True, is_vegan=True, calories=100),
                    DishItem(name="Kheer", is_vegetarian=True, calories=190, allergens=["dairy", "nuts"]),
                ],
            ),
        ],
        special_note="Wednesday is Biryani Night! 🍗",
    ),
    DayMenu(
        day=DayOfWeek.THURSDAY,
        meals=[
            Meal(
                meal_type=MealType.BREAKFAST,
                start_time="07:30",
                end_time="09:30",
                items=[
                    DishItem(name="Chole Bhature", is_vegetarian=True, calories=420, allergens=["gluten"]),
                    DishItem(name="Tea/Coffee", is_vegetarian=True, calories=30),
                    DishItem(name="Bread & Butter", is_vegetarian=True, calories=200, allergens=["gluten", "dairy"]),
                    DishItem(name="Boiled Eggs", is_vegetarian=False, calories=155),
                ],
            ),
            Meal(
                meal_type=MealType.LUNCH,
                start_time="12:00",
                end_time="14:00",
                items=[
                    DishItem(name="Rice", is_vegetarian=True, is_vegan=True, calories=200),
                    DishItem(name="Chana Dal", is_vegetarian=True, is_vegan=True, calories=160),
                    DishItem(name="Mix Veg Curry", is_vegetarian=True, is_vegan=True, calories=170),
                    DishItem(name="Fish Fry", is_vegetarian=False, calories=300),
                    DishItem(name="Chapati", is_vegetarian=True, is_vegan=True, calories=120, allergens=["gluten"]),
                    DishItem(name="Salad", is_vegetarian=True, is_vegan=True, calories=30),
                ],
            ),
            Meal(
                meal_type=MealType.SNACKS,
                start_time="17:00",
                end_time="18:00",
                items=[
                    DishItem(name="Aloo Tikki", is_vegetarian=True, calories=200),
                    DishItem(name="Tea", is_vegetarian=True, calories=30, allergens=["dairy"]),
                ],
            ),
            Meal(
                meal_type=MealType.DINNER,
                start_time="19:30",
                end_time="21:30",
                items=[
                    DishItem(name="Rice", is_vegetarian=True, is_vegan=True, calories=200),
                    DishItem(name="Dal Fry", is_vegetarian=True, is_vegan=True, calories=155),
                    DishItem(name="Palak Paneer", is_vegetarian=True, calories=260, allergens=["dairy"]),
                    DishItem(name="Chapati", is_vegetarian=True, is_vegan=True, calories=120, allergens=["gluten"]),
                    DishItem(name="Rasgulla", is_vegetarian=True, calories=150, allergens=["dairy"]),
                ],
            ),
        ],
    ),
    DayMenu(
        day=DayOfWeek.FRIDAY,
        meals=[
            Meal(
                meal_type=MealType.BREAKFAST,
                start_time="07:30",
                end_time="09:30",
                items=[
                    DishItem(name="Dosa with Sambhar", is_vegetarian=True, is_vegan=True, calories=270),
                    DishItem(name="Coconut Chutney", is_vegetarian=True, is_vegan=True, calories=50),
                    DishItem(name="Tea/Coffee", is_vegetarian=True, calories=30),
                    DishItem(name="Boiled Eggs", is_vegetarian=False, calories=155),
                    DishItem(name="Cornflakes with Milk", is_vegetarian=True, calories=200, allergens=["dairy"]),
                ],
            ),
            Meal(
                meal_type=MealType.LUNCH,
                start_time="12:00",
                end_time="14:00",
                items=[
                    DishItem(name="Lemon Rice", is_vegetarian=True, is_vegan=True, calories=230),
                    DishItem(name="Rajma", is_vegetarian=True, is_vegan=True, calories=210),
                    DishItem(name="Chapati", is_vegetarian=True, is_vegan=True, calories=120, allergens=["gluten"]),
                    DishItem(name="Raita", is_vegetarian=True, calories=70, allergens=["dairy"]),
                    DishItem(name="Salad", is_vegetarian=True, is_vegan=True, calories=30),
                ],
            ),
            Meal(
                meal_type=MealType.SNACKS,
                start_time="17:00",
                end_time="18:00",
                items=[
                    DishItem(name="Pav Bhaji", is_vegetarian=True, calories=350, allergens=["gluten", "dairy"]),
                    DishItem(name="Tea", is_vegetarian=True, calories=30, allergens=["dairy"]),
                ],
            ),
            Meal(
                meal_type=MealType.DINNER,
                start_time="19:30",
                end_time="21:30",
                items=[
                    DishItem(name="Rice", is_vegetarian=True, is_vegan=True, calories=200),
                    DishItem(name="Dal Tadka", is_vegetarian=True, is_vegan=True, calories=150),
                    DishItem(name="Butter Chicken", is_vegetarian=False, calories=400, allergens=["dairy"]),
                    DishItem(name="Paneer Tikka Masala", is_vegetarian=True, calories=310, allergens=["dairy"]),
                    DishItem(name="Naan", is_vegetarian=True, calories=260, allergens=["gluten", "dairy"]),
                    DishItem(name="Jalebi", is_vegetarian=True, calories=250, allergens=["gluten"]),
                ],
            ),
        ],
        special_note="Friday Special: Butter Chicken & Naan Night! 🎉",
    ),
    DayMenu(
        day=DayOfWeek.SATURDAY,
        meals=[
            Meal(
                meal_type=MealType.BREAKFAST,
                start_time="08:00",
                end_time="10:00",
                items=[
                    DishItem(name="Puri Bhaji", is_vegetarian=True, calories=380, allergens=["gluten"]),
                    DishItem(name="Tea/Coffee", is_vegetarian=True, calories=30),
                    DishItem(name="Bread & Jam", is_vegetarian=True, calories=180, allergens=["gluten"]),
                    DishItem(name="Boiled Eggs", is_vegetarian=False, calories=155),
                ],
            ),
            Meal(
                meal_type=MealType.LUNCH,
                start_time="12:00",
                end_time="14:00",
                items=[
                    DishItem(name="Rice", is_vegetarian=True, is_vegan=True, calories=200),
                    DishItem(name="Sambhar", is_vegetarian=True, is_vegan=True, calories=140),
                    DishItem(name="Bhindi Masala", is_vegetarian=True, is_vegan=True, calories=160),
                    DishItem(name="Chapati", is_vegetarian=True, is_vegan=True, calories=120, allergens=["gluten"]),
                    DishItem(name="Pickle & Papad", is_vegetarian=True, is_vegan=True, calories=50),
                ],
            ),
            Meal(
                meal_type=MealType.SNACKS,
                start_time="17:00",
                end_time="18:00",
                items=[
                    DishItem(name="Maggi Noodles", is_vegetarian=True, calories=320, allergens=["gluten"]),
                    DishItem(name="Tea", is_vegetarian=True, calories=30, allergens=["dairy"]),
                ],
            ),
            Meal(
                meal_type=MealType.DINNER,
                start_time="19:30",
                end_time="21:30",
                items=[
                    DishItem(name="Veg Pulao", is_vegetarian=True, is_vegan=True, calories=280),
                    DishItem(name="Dal Makhani", is_vegetarian=True, calories=200, allergens=["dairy"]),
                    DishItem(name="Mutton Curry", is_vegetarian=False, calories=420),
                    DishItem(name="Chapati", is_vegetarian=True, is_vegan=True, calories=120, allergens=["gluten"]),
                    DishItem(name="Fruit Custard", is_vegetarian=True, calories=180, allergens=["dairy"]),
                ],
            ),
        ],
        special_note="Saturday Night: Mutton Curry Special 🍖",
    ),
    DayMenu(
        day=DayOfWeek.SUNDAY,
        meals=[
            Meal(
                meal_type=MealType.BREAKFAST,
                start_time="08:00",
                end_time="10:30",
                items=[
                    DishItem(name="Stuffed Paratha (Aloo/Gobi)", is_vegetarian=True, calories=320, allergens=["gluten"]),
                    DishItem(name="Curd", is_vegetarian=True, calories=60, allergens=["dairy"]),
                    DishItem(name="Pickle", is_vegetarian=True, is_vegan=True, calories=10),
                    DishItem(name="Tea/Coffee", is_vegetarian=True, calories=30),
                    DishItem(name="Omelette", is_vegetarian=False, calories=180),
                ],
            ),
            Meal(
                meal_type=MealType.LUNCH,
                start_time="12:30",
                end_time="14:30",
                items=[
                    DishItem(name="Rice", is_vegetarian=True, is_vegan=True, calories=200),
                    DishItem(name="Dal Fry", is_vegetarian=True, is_vegan=True, calories=155),
                    DishItem(name="Shahi Paneer", is_vegetarian=True, calories=300, allergens=["dairy", "nuts"]),
                    DishItem(name="Chapati", is_vegetarian=True, is_vegan=True, calories=120, allergens=["gluten"]),
                    DishItem(name="Salad", is_vegetarian=True, is_vegan=True, calories=30),
                    DishItem(name="Sweet Lassi", is_vegetarian=True, calories=150, allergens=["dairy"]),
                ],
            ),
            Meal(
                meal_type=MealType.SNACKS,
                start_time="17:00",
                end_time="18:00",
                items=[
                    DishItem(name="Spring Roll", is_vegetarian=True, calories=180, allergens=["gluten"]),
                    DishItem(name="Cold Coffee", is_vegetarian=True, calories=150, allergens=["dairy"]),
                ],
            ),
            Meal(
                meal_type=MealType.DINNER,
                start_time="19:30",
                end_time="21:30",
                items=[
                    DishItem(name="Rice", is_vegetarian=True, is_vegan=True, calories=200),
                    DishItem(name="Yellow Dal", is_vegetarian=True, is_vegan=True, calories=135),
                    DishItem(name="Chicken Do Pyaza", is_vegetarian=False, calories=380),
                    DishItem(name="Matar Paneer", is_vegetarian=True, calories=250, allergens=["dairy"]),
                    DishItem(name="Chapati", is_vegetarian=True, is_vegan=True, calories=120, allergens=["gluten"]),
                    DishItem(name="Gajar Halwa", is_vegetarian=True, calories=280, allergens=["dairy", "nuts"]),
                ],
            ),
        ],
        special_note="Sunday Special Brunch — Extended breakfast hours! ☕",
    ),
]


# ─── Nutrition Database ──────────────────────────────────────────────────────────

NUTRITION_DB: dict[str, NutritionInfo] = {
    "paneer butter masala": NutritionInfo(
        dish_name="Paneer Butter Masala", calories=280, protein_g=14.0, carbs_g=12.0,
        fat_g=20.0, fiber_g=2.0, is_vegetarian=True, is_vegan=False, allergens=["dairy"]
    ),
    "dal tadka": NutritionInfo(
        dish_name="Dal Tadka", calories=150, protein_g=9.0, carbs_g=22.0,
        fat_g=3.5, fiber_g=5.0, is_vegetarian=True, is_vegan=True, allergens=[]
    ),
    "chicken curry": NutritionInfo(
        dish_name="Chicken Curry", calories=350, protein_g=28.0, carbs_g=8.0,
        fat_g=22.0, fiber_g=1.5, is_vegetarian=False, is_vegan=False, allergens=[]
    ),
    "butter chicken": NutritionInfo(
        dish_name="Butter Chicken", calories=400, protein_g=30.0, carbs_g=10.0,
        fat_g=26.0, fiber_g=1.0, is_vegetarian=False, is_vegan=False, allergens=["dairy"]
    ),
    "chapati": NutritionInfo(
        dish_name="Chapati", calories=120, protein_g=3.5, carbs_g=22.0,
        fat_g=2.5, fiber_g=2.0, is_vegetarian=True, is_vegan=True, allergens=["gluten"]
    ),
    "rice": NutritionInfo(
        dish_name="Rice (Steamed)", calories=200, protein_g=4.0, carbs_g=45.0,
        fat_g=0.5, fiber_g=0.5, is_vegetarian=True, is_vegan=True, allergens=[]
    ),
    "samosa": NutritionInfo(
        dish_name="Samosa", calories=250, protein_g=5.0, carbs_g=30.0,
        fat_g=12.0, fiber_g=2.0, is_vegetarian=True, is_vegan=True, allergens=["gluten"]
    ),
    "chole masala": NutritionInfo(
        dish_name="Chole Masala", calories=200, protein_g=10.0, carbs_g=28.0,
        fat_g=6.0, fiber_g=8.0, is_vegetarian=True, is_vegan=True, allergens=[]
    ),
    "rajma": NutritionInfo(
        dish_name="Rajma", calories=210, protein_g=12.0, carbs_g=30.0,
        fat_g=5.0, fiber_g=9.0, is_vegetarian=True, is_vegan=True, allergens=[]
    ),
    "gulab jamun": NutritionInfo(
        dish_name="Gulab Jamun", calories=175, protein_g=3.0, carbs_g=28.0,
        fat_g=6.0, fiber_g=0.5, is_vegetarian=True, is_vegan=False, allergens=["dairy", "gluten"]
    ),
    "veg biryani": NutritionInfo(
        dish_name="Veg Biryani", calories=350, protein_g=8.0, carbs_g=55.0,
        fat_g=10.0, fiber_g=3.0, is_vegetarian=True, is_vegan=False, allergens=[]
    ),
    "chicken biryani": NutritionInfo(
        dish_name="Chicken Biryani", calories=450, protein_g=22.0, carbs_g=52.0,
        fat_g=16.0, fiber_g=2.0, is_vegetarian=False, is_vegan=False, allergens=[]
    ),
    "idli sambhar": NutritionInfo(
        dish_name="Idli Sambhar", calories=230, protein_g=8.0, carbs_g=42.0,
        fat_g=3.0, fiber_g=4.0, is_vegetarian=True, is_vegan=True, allergens=[]
    ),
    "dosa with sambhar": NutritionInfo(
        dish_name="Dosa with Sambhar", calories=270, protein_g=7.0, carbs_g=40.0,
        fat_g=8.0, fiber_g=3.5, is_vegetarian=True, is_vegan=True, allergens=[]
    ),
    "palak paneer": NutritionInfo(
        dish_name="Palak Paneer", calories=260, protein_g=15.0, carbs_g=10.0,
        fat_g=18.0, fiber_g=3.0, is_vegetarian=True, is_vegan=False, allergens=["dairy"]
    ),
}


# ─── Special / Festival Menus ────────────────────────────────────────────────────

SPECIAL_MENUS: list[dict] = [
    {
        "name": "Independence Day Special",
        "date": "2026-08-15",
        "items": ["Tiranga Pulao", "Paneer Tikka", "Gulab Jamun", "Mango Lassi", "Special Biryani"],
        "note": "Tricolor-themed lunch with festive sweets 🇮🇳"
    },
    {
        "name": "Diwali Feast",
        "date": "2026-10-20",
        "items": ["Puri", "Chole", "Paneer Makhani", "Gulab Jamun", "Rasgulla", "Kaju Katli", "Jalebi"],
        "note": "Festival of lights celebration dinner 🪔"
    },
    {
        "name": "Founders' Day Dinner",
        "date": "2026-11-25",
        "items": ["Mughlai Biryani", "Seekh Kebab", "Shahi Paneer", "Naan", "Phirni", "Ice Cream"],
        "note": "Grand dinner celebrating the university's founding anniversary 🎓"
    },
]


# ─── Data Access Functions ───────────────────────────────────────────────────────

def get_todays_menu(meal: str | None = None) -> dict:
    """Get today's menu. Optionally filter by meal type."""
    import datetime
    day_name = datetime.datetime.now().strftime("%A")
    for day_menu in WEEKLY_MENU:
        if day_menu.day.value == day_name:
            menu_data = day_menu.model_dump()
            if meal:
                meal_upper = meal.capitalize()
                menu_data["meals"] = [
                    m for m in menu_data["meals"]
                    if m["meal_type"] == meal_upper
                ]
            return menu_data
    # Fallback to Monday if day not found
    fallback = WEEKLY_MENU[0].model_dump()
    fallback["note"] = f"Showing Monday menu as fallback (current day: {day_name})"
    return fallback


def get_weekly_menu(day: str | None = None) -> list[dict]:
    """Get the full weekly menu or a specific day's menu."""
    if day:
        day_lower = day.lower()
        return [m.model_dump() for m in WEEKLY_MENU if m.day.value.lower() == day_lower]
    return [m.model_dump() for m in WEEKLY_MENU]


def get_nutrition_info(dish_name: str) -> dict | None:
    """Get nutritional info for a dish."""
    key = dish_name.lower().strip()
    info = NUTRITION_DB.get(key)
    if info:
        return info.model_dump()
    # Fuzzy search
    for db_key, db_info in NUTRITION_DB.items():
        if key in db_key or db_key in key:
            return db_info.model_dump()
    return None


def get_mess_timings() -> list[dict]:
    """Get mess operating hours."""
    return [t.model_dump() for t in MESS_TIMINGS]


def get_special_menus() -> list[dict]:
    """Get upcoming special/festival menus."""
    return SPECIAL_MENUS
