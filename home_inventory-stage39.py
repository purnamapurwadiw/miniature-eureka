# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: HomeInventory
def usage_scenarios():
    """Демонстрирует основные сценарии работы с HomeInventory.

    Сценарий 1: Регистрация нового предмета в комнате.
    Сценарий 2: Поиск предметов по категории и статусу гарантии.
    Сценарий 3: Вывод отчета по всем предметам с истекшей гарантией.
    Сценарий 4: Фильтрация предметов по дате покупки и цене.
    Сценарий 5: Удаление предмета из каталога.
    """
    # Сценарий 1: Регистрация нового предмета
    room = Room(name="Кухня")
    item = Item(name="Микроволновка", category="Электроника",
                purchase_date="2023-01-15", purchase_price=5000,
                warranty_months=12, warranty_expires="2024-01-15",
                description="Белая микроволновка Samsung")
    room.add_item(item)

    # Сценарий 2: Поиск с фильтром по категории и статусу гарантии
    items = home_inventory.search(category="Электроника",
                                  warranty_expired=True)
    for i in items:
        print(f"{i.name} - гарантия истекла: {i.warranty_expired}")

    # Сценарий 3: Отчет о предметах с истекшей гарантией
    expired = home_inventory.get_items_with_expired_warranty()
    if expired:
        print("Предметы с истекшей гарантией:")
        for i in expired:
            print(f"  - {i.name} (куплена: {i.purchase_date})")
    else:
        print("Все предметы находятся в порядке.")

    # Сценарий 4: Фильтрация по цене и дате покупки
    cheap_items = home_inventory.get_items(
        max_price=3000, min_purchase_date="2023-06-01")
    if cheap_items:
        print("Недорогие предметы, купленные после июня 2023:")
        for i in cheap_items:
            print(f"  - {i.name}: {i.purchase_price}")

    # Сценарий 5: Удаление предмета
    home_inventory.remove_item(item)
    print(f"Удалён предмет: {item.name}")
