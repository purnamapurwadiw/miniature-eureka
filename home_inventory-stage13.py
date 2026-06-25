# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: HomeInventory
def search_items(query: str) -> list[dict]:
    query_lower = query.lower()
    results = []
    for item in items:
        if (query_lower in item['name'].lower() or
            any(query_lower == cat.lower() for cat in item.get('categories', [])) or
            query_lower in item.get('room', '').lower()):
            results.append(item)
    return results
