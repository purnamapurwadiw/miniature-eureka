# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: HomeInventory
def generate_summary():
    rooms = {r['name']: len(r.get('items', [])) for r in inventory_data.values()}
    categories = {}
    for item in inventory_data.values():
        cat = item.get('category') or 'Uncategorized'
        categories[cat] = categories.get(cat, 0) + 1
    total_items = len(inventory_data)
    print(f"Сводка: всего предметов {total_items}, комнат {len(rooms)}, категорий {len(categories)}")
    for room, count in rooms.items():
        if count > 0:
            print(f"  {room}: {count} предметов")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  Категория '{cat}': {count} предметов")
