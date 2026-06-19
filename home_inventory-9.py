# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: HomeInventory
import json, re, sys
from datetime import datetime
INITIAL_DATA = '''{"rooms": ["Кухня", "Спальня"], "categories": {"Кухня": ["Посуда", "Техника"]}, "items": [{"id": 1, "name": "Чайник", "room": "Кухня", "category": "Техника", "warranty_months": 24}]}'''
def parse_initial_data(data_str: str) -> dict:
    try:
        data = json.loads(data_str)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        return {}
    if not isinstance(data, dict):
        print("Некорректный формат начальных данных", file=sys.stderr)
        return {}
    for key in ["rooms", "categories", "items"]:
        if key not in data or (key == "items" and not isinstance(data[key], list)):
            print(f"Отсутствует обязательное поле '{key}'", file=sys.stderr)
            return {}
    now = datetime.now()
    for item in data["items"]:
        if "created_at" not in item:
            item["created_at"] = now.isoformat()
        elif isinstance(item["created_at"], str):
            try:
                dt = datetime.fromisoformat(item["created_at"].replace("Z", "+00:00"))
                item["created_at_dt"] = dt
            except ValueError:
                pass
    return data
