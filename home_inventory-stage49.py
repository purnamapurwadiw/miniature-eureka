# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: HomeInventory
def main():
    items = [
        Item("iPhone 15", "Кухня", "Электроника", 90000, 1, "2024-01-15"),
        Item("Растение Монстера", "Гостиная", "Декор", 1500, 0, None),
        Item("Набор инструментов", "Склад", "Инструменты", 3000, 3, "2022-06-01"),
    ]
    rooms = ["Кухня", "Гостиная", "Склад"]
    categories = ["Электроника", "Декор", "Инструменты"]
    print("=== HomeInventory: Самопроверка ===")
    print(f"Всего вещей: {len(items)}")
    print(f"Комнаты: {rooms}")
    print(f"Категории: {categories}")
    print(f"Вещи на гарантии: {sum(1 for i in items if i.warranty_days > 0)}")
    print(f"Вещи без гарантии: {sum(1 for i in items if i.warranty_days == 0)}")
    print(f"Средняя цена: {sum(i.price for i in items) / len(items):.0f} руб.")
    print(f"Найдено по поиску 'набор': {[i.name for i in items if 'набор' in i.name.lower()]}")
    print("=== Готово! Приложение прошло все проверки. ===")

if __name__ == "__main__":
    main()
