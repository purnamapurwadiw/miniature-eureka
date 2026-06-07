# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: HomeInventory
import json
from datetime import datetime, timedelta

# Базовая структура данных: комнаты, категории и список вещей
ROOMS = ["Кухня", "Спальня", "Гостиная"]
CATEGORIES = ["Электроника", "Посуда", "Одежда", "Другое"]

class Item:
    def __init__(self, name, room, category, warranty_months=0):
        self.name = name
        self.room = room
        self.category = category
        self.purchase_date = datetime.now() - timedelta(days=warranty_months * 30)
        self.warranty_months = warranty_months

    def is_warranty_active(self):
        return (datetime.now() - self.purchase_date).days <= self.warranty_months * 30

    def to_dict(self):
        return {
            "name": self.name,
            "room": self.room,
            "category": self.category,
            "purchase_date": self.purchase_date.strftime("%Y-%m-%d"),
            "warranty_months": self.warranty_months,
            "is_warranty_active": self.is_warranty_active()
        }

# Демонстрационные данные
demo_items = [
    Item("Смартфон", "Спальня", "Электроника", 12),
    Item("Кофеварка", "Кухня", "Электроника", 24),
    Item("Чашки", "Кухня", "Посуда", 0),
    Item("Диван", "Гостиная", "Другое", 36)
]

# Сохранение в JSON для демонстрации (в реальном проекте - в БД или файл)
def save_inventory(items):
    with open("inventory.json", "w", encoding="utf-8") as f:
        json.dump([item.to_dict() for item in items], f, ensure_ascii=False, indent=2)

save_inventory(demo_items)
print(f"Инициализировано {len(demo_items)} вещей. Данные сохранены в inventory.json")
