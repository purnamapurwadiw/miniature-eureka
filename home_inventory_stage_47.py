# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: HomeInventory
def demo():
    rooms = Room("Kitchen", Room("Living", Room("Bedroom")))
    cat_electronics = Category("Electronics")
    cat_clothes = Category("Clothes")
    cat_garden = Category("Garden")

    items = [
        Item("TV", "Samsung", cat_electronics),
        Item("Sofa", "IKEA", cat_clothes),
        Item("Garden Chair", "Home Depot", cat_garden),
        Item("Garden Hose", "Home Depot", cat_garden),
    ]
    inventory = HomeInventory(rooms, items)

    inventory.add_item(Item("Laptop", "Apple", cat_electronics))
    inventory.add_item(Item("T-Shirt", "H&M", cat_clothes))

    inventory.add_room(Room("Garage"))
    inventory.add_category(Category("Tools"))
    inventory.add_item(Item("Drill", "Makita", Category("Tools")))

    inventory.set_warranty(Item("TV"), Warranty("2 years"))
    inventory.set_warranty(Item("Sofa"), Warranty("5 years"))

    print("=== HomeInventory Demo ===")
    print(f"Total items: {inventory.count}")
    print(f"Total rooms: {inventory.total_rooms}")
    print(f"Total categories: {inventory.total_categories}")

    print("\n--- By room ---")
    for room in inventory.rooms.values():
        print(f"\nRoom: {room.name}")
        for item in room.items:
            print(f"  - {item.name} ({item.brand})")

    print("\n--- By category ---")
    for cat in inventory.categories.values():
        print(f"\nCategory: {cat.name}")
        for item in cat.items:
            print(f"  - {item.name} ({item.brand})")

    print("\n--- Search ---")
    print(f"Search 'electronic': {inventory.search('electronic').count} items")
    print(f"Search 'garage': {inventory.search('garage').count} items")

    print("\n--- Warranty ---")
    for item in inventory.items:
        print(f"{item.name}: {item.warranty}")

    print("\n--- Sort ---")
    sorted_items = inventory.sort_by_name()
    for item in sorted_items:
        print(f"  - {item.name}")

    print("\n--- Update ---")
    inventory.update_item(Item("TV", "LG", cat_electronics))
    for item in inventory.items:
        print(f"{item.name}: {item.brand} (room: {item.room.name})")

    print("\n--- Delete ---")
    inventory.delete_item(Item("Garden Hose"))
    print(f"Total items after delete: {inventory.count}")

    print("\nDemo complete!")
