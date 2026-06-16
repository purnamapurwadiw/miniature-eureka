# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: HomeInventory
def sort_items(items, key='date', reverse=False):
    if not items: return []
    def get_sort_key(item):
        val = item.get(key)
        if isinstance(val, str):
            try: int(val); is_num=True
            except ValueError: is_num=False; val=val.lower()
        else: is_num=isinstance(val, (int, float)); val=float('-inf') if not reverse and key=='date' else val
        return (not is_num, 0 if is_num else -1) if reverse else (is_num, 1 if is_num else 0), val
    sorted_items = sorted(items, key=get_sort_key)
    if key == 'name': sorted_items.sort(key=lambda x: x.get('name', '').lower())
    elif key == 'priority': sorted_items.sort(key=lambda x: -x.get('priority', 0))
    return sorted_items
