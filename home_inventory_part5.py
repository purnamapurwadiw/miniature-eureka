# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: HomeInventory
def delete_item(item_id: int) -> bool:
    if item_id not in items_db:
        print(f"Ошибка: запись с ID {item_id} не найдена.")
        return False
    
    room = items_db[item_id]
    
    # Проверка на наличие гарантии и уведомление при удалении
    if room.get('warranty_end_date'):
        warranty_days_left = (datetime.date.today() - datetime.datetime.strptime(room['warranty_end_date'], '%Y-%m-%d').date()).days
        print(f"Уведомление: у предмета {room['name']} истекает гарантия через {max(0, warranty_days_left)} дней.")

    # Удаление из базы данных
    del items_db[item_id]
    
    if room.get('category'):
        category = room['category']
        if category in categories_db and item_id in categories_db[category]:
            categories_db[category].remove(item_id)
            
    print(f"Предмет '{room['name']}' успешно удален.")
    return True

def delete_room(room_name: str) -> bool:
    # Поиск комнаты в базе данных (предполагается, что rooms_db хранит список комнат или их ID)
    # Для простоты предположим, что у нас есть словарь rooms_db где ключ - имя комнаты
    if room_name not in rooms_db:
        print(f"Ошибка: комната '{room_name}' не найдена.")
        return False
    
    items_to_delete = [item_id for item_id, data in items_db.items() if data.get('room') == room_name]
    
    # Удаление предметов из категории и базы данных перед удалением комнаты
    for item_id in items_to_delete:
        delete_item(item_id)
        
    del rooms_db[room_name]
    print(f"Комната '{room_name}' успешно удалена вместе со всеми её предметами.")
    return True

def handle_missing_ids(operation_func, *args):
    """Обертка для обработки отсутствующих идентификаторов с единой логикой."""
    try:
        result = operation_func(*args)
        if not isinstance(result, bool):
            print("Ошибка: функция должна возвращать булево значение.")
            return False
        return result
    except KeyError as e:
        print(f"Критическая ошибка: отсутствующий ключ в базе данных - {e}")
        return False
    except Exception as e:
        print(f"Неожиданная ошибка при выполнении операции: {type(e).__name__}: {e}")
        return False
