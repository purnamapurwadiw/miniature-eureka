# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: HomeInventory
def edit_item(item_id, new_data):
    if not isinstance(new_data, dict):
        raise ValueError("new_data должен быть словарем")
    
    updated_item = None
    for item in inventory:
        if item['id'] == item_id:
            updated_item = item.copy()
            if 'name' in new_data and new_data['name']:
                updated_item['name'] = new_data['name']
            if 'room' in new_data and new_data['room']:
                updated_item['room'] = new_data['room']
            if 'category' in new_data and new_data['category']:
                updated_item['category'] = new_data['category']
            if 'warranty_months' in new_data:
                updated_item['warranty_months'] = int(new_data['warranty_months'])
            if 'notes' in new_data and new_data['notes']:
                updated_item['notes'] = new_data['notes']
            break
    
    if updated_item:
        inventory.remove(updated_item)
        inventory.append(updated_item)
        print(f"Запись с ID {item_id} успешно обновлена.")
        return updated_item
    else:
        print(f"Запись с ID {item_id} не найдена для редактирования.")
        return None
