# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: HomeInventory
import sys

def print_metrics():
    rooms = set()
    categories = set()
    items_by_room = {}
    warranty_items = 0
    for line in open(sys.argv[1] if len(sys.argv) > 1 else "home_inventory.py"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("def ") or line.startswith("import ") or line.startswith("@"):
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip("'").strip('"')
            if key == "rooms":
                for r in rooms_str.split(","):
                    r = r.strip().strip("'").strip('"')
                    if r:
                        rooms.add(r)
                        items_by_room.setdefault(r, 0)
            elif key == "categories":
                for c in cats_str.split(","):
                    c = c.strip().strip("'").strip('"')
                    if c:
                        categories.add(c)
            elif key == "items" and val:
                try:
                    items_by_room.setdefault(val, 0)
                    warranty_items += int(warranty_val)
                except (ValueError, TypeError):
                    pass
    print(f"Комнаты: {len(rooms)}")
    print(f"Категории: {len(categories)}")
    print(f"Всего предметов: {sum(items_by_room.values())}")
    print(f"С гарантией: {warranty_items}")

print_metrics()
