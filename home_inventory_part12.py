# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: HomeInventory
def load_inventory_from_json(filepath: str) -> list[dict]:
    import json
    from pathlib import Path
    
    if not Path(filepath).exists():
        print(f"Файл {filepath} не найден.")
        return []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict) and "items" in data:
            items = data["items"]
        else:
            print("Некорректный формат JSON. Ожидается список или объект с ключом 'items'.")
            return []
        
        for i, item in enumerate(items):
            if not isinstance(item, dict):
                print(f"Ошибка в строке {i}: элемент не является словарем.")
                continue
            
            # Простая нормализация данных (опционально)
            if "room" not in item:
                item["room"] = "Не указано"
            
        return items
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON файла {filepath}: {e}")
        return []
    except Exception as e:
        print(f"Произошла неизвестная ошибка при чтении {filepath}: {e}")
        return []
