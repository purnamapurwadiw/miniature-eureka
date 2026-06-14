# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: HomeInventory
def filter_items(status=None, category=None, tags=None):
    filtered = []
    for item in items:
        if status and item.get('status') != status:
            continue
        if category and item.get('category') != category:
            continue
        if tags:
            item_tags = item.get('tags', [])
            if not any(tag.lower() in t.lower() for tag in tags.split() for t in item_tags):
                continue
        filtered.append(item)
    return filtered
