# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: HomeInventory
def display_item(item):
    """Выводит компактную строку с деталями товара."""
    if item is None:
        print("  — нет записей")
        return
    print(f"  [{item.room}] {item.name} ({item.category})")
    price = f"{item.price:.2f}" if isinstance(item.price, float) else item.price
    print(f"    Цена: {price}")
    if item.warranty_years > 0:
        print(f"    Гарантия: {item.warranty_years} лет")
    if getattr(item, 'quantity', None):
        print(f"    Остаток: {item.quantity}")
    if getattr(item, 'location', None):
        print(f"    Место: {item.location}")

def display_inventory(items=None):
    """Показывает список товаров с группировкой по комнате."""
    items = items or []
    rooms = {}
    for it in items:
        r = getattr(it, 'room', 'Без комнаты')
        rooms.setdefault(r, []).append(it)

    for room_name in sorted(rooms):
        print(f"\n📦 {room_name} ({len(rooms[room_name])})")
        for it in rooms[room_name]:
            display_item(it)

if __name__ == "__main__":
    from data import items as _items
    display_inventory(_items)
