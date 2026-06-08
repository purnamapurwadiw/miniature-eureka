# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: HomeInventory
class Item:
    def __init__(self, name, room, category, warranty_months):
        self.name = name
        self.room = room
        self.category = category
        self.warranty_months = warranty_months

    def is_warranty_active(self, current_date):
        from datetime import datetime
        expiry_date = datetime.strptime(f"{current_date.year}-{current_date.month}-{current_date.day}", "%Y-%m-%d") + timedelta(days=30)
        return expiry_date > datetime.now()

class Room:
    def __init__(self, name):
        self.name = name

class Category:
    def __init__(self, name):
        self.name = name

def validate_input(name, room, category, warranty_months):
    if not name or len(name.strip()) == 0:
        raise ValueError("Name cannot be empty.")
    if not room or len(room.strip()) == 0:
        raise ValueError("Room cannot be empty.")
    if not category or len(category.strip()) == 0:
        raise ValueError("Category cannot be empty.")
    if warranty_months < 0:
        raise ValueError("Warranty months cannot be negative.")
    return True

from datetime import date, timedelta
