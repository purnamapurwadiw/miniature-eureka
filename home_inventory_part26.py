# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: HomeInventory
def run_demo_commands():
    """Набор демо-команд для ручного тестирования HomeInventory."""
    print("=== Демо HomeInventory ===")
    
    # Добавим несколько вещей и комнат для демонстрации
    room = Room(name="Кухня", description="Где готовим еду")
    item1 = Item(name="Сковорода", category=Category(name="Посуда"), warranty=Warranty(years=5, active=True))
    item2 = Item(name="Робот-пылесос", category=Category(name="Техника"), warranty=Warranty(years=2, active=False))
    item3 = Item(name="Миска для кота", category=Category(name="Питомцы"), warranty=Warranty(years=10, active=True))
    
    room.add_item(item1)
    room.add_item(item2)
    room.add_item(item3)
    
    print(f"\nКомната: {room.name}")
    for item in room.items:
        print(f"  - {item.name} ({item.category.name}) — гарантия активна: {item.warranty.active}")
    
    # Поиск по комнате и категории
    kitchen_items = search_by_room(room)
    active_pots = search_by_category(items, Category(name="Посуда"), warranty_active=True)
    
    print(f"\nПредметы на кухне: {len(kitchen_items)}")
    print(f"Активная посуда с гарантией: {len(active_pots)}")
    
    # Статистика по всем предметам в доме
    total = sum(len(r.items) for r in rooms)
    active_warranty_count = sum(1 for item in items if item.warranty.active and item.warranty.years > 0)
    
    print(f"\nВсего предметов: {total}")
    print(f"Предметы с активной гарантией: {active_warranty_count}")

run_demo_commands()
