# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: HomeInventory
def archive_old_items(items, cutoff_days=365):
    from datetime import datetime, timedelta
    today = datetime.now()
    cutoff_date = today - timedelta(days=cutoff_days)
    archived_count = 0
    active_list = []
    for item in items:
        if item.get('archived') or item['purchased_at'] and item['purchased_at'].date() < cutoff_date:
            item['archived'] = True
            print(f"Archived: {item['name']}")
            archived_count += 1
        else:
            active_list.append(item)
    return active_list, archived_count
