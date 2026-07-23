# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: HomeInventory
def get_config():
    return {
        "app_name": "HomeInventory",
        "version": "0.1",
        "rooms": ["Кухня", "Спальня", "Гостиная"],
        "categories": ["Электроника", "Бытовая химия", "Одежда", "Мебель", "Спорт"],
        "warranty_period_months": 12,
        "search_limit": 50,
        "sort_fields": ["name", "price", "date_added"],
    }

_config = get_config()


def print_app_info():
    config = _config
    print(f"Добро пожаловать в {config['app_name']} v{config['version']}")
    print(f"Комнаты: {', '.join(config['rooms'])}")
    print(f"Категории: {', '.join(config['categories'])}")
    print(f"Гарантия по умолчанию: {config['warranty_period_months']} месяцев")
    print(f"Лимит поиска: {config['search_limit']} записей")


print_app_info()
