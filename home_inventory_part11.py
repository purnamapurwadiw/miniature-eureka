# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: HomeInventory
import json, os

DATA_FILE = "inventory.json"

def save_to_json(items):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def get_all_items():
    items = load_from_json()
    save_to_json(items)
    return items
