# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: HomeInventory
def show_inventory():
    """Отображает отсортированный каталог вещей с ключевой информацией."""
    if not items:
        print("📋 Каталог пуст. Добавьте предметы!")
        return
    print("\n🏠 ДОМАШНИЙ КАТАЛОГ\n" + "=" * 50)
    for idx, item in enumerate(items, 1):
        print(f"\n[{idx}] {item.name} ({item.room})")
        print(f"    Категория: {item.category}")
        if item.quantity:
            print(f"    Количество: {item.quantity}")
        if item.warranty:
            print(f"    Гарантия: до {item.warranty} года(лет)")
        if item.location:
            print(f"    Место: {item.location}")
        if item.price:
            print(f"    Цена: {item.price} ₽")
        if item.notes:
            print(f"    Заметки: {item.notes}")
    print("\n" + "=" * 50 + "\n")


def find_item(query):
    """Поиск предметов по части имени, категории, комнате или заметкам."""
    if not query:
        return []
    query_lower = query.lower()
    matches = []
    for item in items:
        if (query_lower in item.name.lower() or
            query_lower in item.category.lower() or
            query_lower in item.room.lower() or
            query_lower in item.notes.lower()):
            matches.append(item)
    return matches


def add_item():
    """Интерактивный ввод нового предмета в каталог."""
    name = input("Название: ")
    if not name:
        return
    room = input(f"Комната [{item.rooms}]: ") or "Разное"
    category = input("Категория: ") or "Разное"
    quantity = input("Количество (опционально): ")
    try:
        quantity = int(quantity) if quantity else 1
    except ValueError:
        print("⚠️ Неверный формат. Количество установлено: 1")
        quantity = 1
    warranty = input("Гарантия (лет, опционально): ")
    try:
        warranty = int(warranty) if warranty else 0
    except ValueError:
        warranty = 0
    location = input("Место хранения (опционально): ")
    price = input("Цена (₽, опционально): ")
    try:
        price = float(price) if price else 0
    except ValueError:
        price = 0
    notes = input("Заметки (опционально): ")
    item = Item(name, room, category, quantity, warranty, location, price, notes)
    items.append(item)
    print(f"✅ Добавлено: {name}")


def edit_item():
    """Редактирование существующего предмета по индексу."""
    if not items:
        print("Нет предметов для редактирования.")
        return
    print("\nСписок предметов:")
    for idx, item in enumerate(items, 1):
        print(f"  {idx}. {item.name} [{item.room}]")
    choice = input("\nВведите номер для редактирования: ")
    try:
        choice = int(choice)
    except ValueError:
        print("⚠️ Введите число.")
        return
    if choice < 1 or choice > len(items):
        print("⚠️ Неверный номер.")
        return
    item = items[choice - 1]
    print(f"\nРедактирование: {item.name}")
    name = input("Название (оставьте пустым, чтобы не менять): ") or item.name
    room = input(f"Комната [{item.room}]: ") or item.room
    category = input("Категория (оставьте пустым, чтобы не менять): ") or item.category
    quantity = input(f"Количество [{item.quantity}]: ")
    try:
        quantity = int(quantity) if quantity else item.quantity
    except ValueError:
        print("⚠️ Неверный формат. Количество не изменено.")
        quantity = item.quantity
    warranty = input(f"Гарантия [{item.warranty}]: ")
    try:
        warranty = int(warranty) if warranty else item.warranty
    except ValueError:
        warranty = item.warranty
    location = input(f"Место [{item.location}]: ") or item.location
    price = input(f"Цена [{item.price}]: ")
    try:
        price = float(price) if price else item.price
    except ValueError:
        price = item.price
    notes = input("Заметки (оставьте пустым, чтобы не менять): ") or item.notes
    item.name = name
    item.room = room
    item.category = category
    item.quantity = quantity
    item.warranty = warranty
    item.location = location
    item.price = price
    item.notes = notes
    print(f"✅ Изменения сохранены для: {item.name}")
