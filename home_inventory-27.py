# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: HomeInventory
def reset_demo_data():
    """Сбрасывает все данные в дефолтные демо-значения."""
    global rooms, categories, items, search_history, settings
    
    rooms = [
        {"name": "Гостиная", "items": []},
        {"name": "Кухня", "items": []},
        {"name": "Спальня", "items": []},
        {"name": "Ванная", "items": []},
        {"name": "Мастерская", "items": []}
    ]
    
    categories = [
        {"name": "Электроника", "icon": "📱"},
        {"name": "Одежда", "icon": "👕"},
        {"name": "Дом и сад", "icon": "🏡"},
        {"name": "Спорт", "icon": "⚽"},
        {"name": "Книги", "icon": "📚"}
    ]
    
    items = [
        {
            "id": 1,
            "title": "Ноутбук",
            "room": "Гостиная",
            "category": "Электроника",
            "quantity": 1,
            "warranty_months": 24,
            "price": 50000,
            "notes": "Для работы и учебы"
        },
        {
            "id": 2,
            "title": "Кроссовки",
            "room": "Спальня",
            "category": "Спорт",
            "quantity": 1,
            "warranty_months": 0,
            "price": 8500,
            "notes": "Беговые"
        },
        {
            "id": 3,
            "title": "Кухонный комбайн",
            "room": "Кухня",
            "category": "Дом и сад",
            "quantity": 1,
            "warranty_months": 12,
            "price": 6500,
            "notes": "Новый"
        }
    ]
    
    search_history = []
    settings = {
        "dark_mode": False,
        "language": "ru",
        "currency": "RUB"
    }

def clear_state():
    """Полностью очищает все данные."""
    global rooms, categories, items, search_history, settings
    
    rooms = []
    categories = []
    items = []
    search_history = []
    settings = {
        "dark_mode": False,
        "language": "ru",
        "currency": "RUB"
    }
