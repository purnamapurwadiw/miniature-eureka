# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: HomeInventory
import re

def sanitize_item_name(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', ' ', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name

def parse_quantity(text: str) -> int:
    m = re.search(r'(\d+)', text)
    return int(m.group(1)) if m else 1

def parse_price(text: str) -> float:
    m = re.search(r'[\d.]+', text)
    return float(m.group()) if m else 0.0

def parse_date(text: str) -> str:
    m = re.search(r'\d{4}-\d{2}-\d{2}', text)
    return m.group() if m else ""

def parse_room(text: str) -> str:
    rooms = ["Кухня", "Спальня", "Гостиная", "Ванная", "Прихожая", "Балкон", "Гараж"]
    for r in rooms:
        if r.lower() in text.lower():
            return r
    return "Другое"
