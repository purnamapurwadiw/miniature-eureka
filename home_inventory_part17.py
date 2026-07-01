# === Stage 17: Добавь группировку записей по категориям ===
# Project: HomeInventory
def group_by_category(items):
    from collections import defaultdict
    grouped = defaultdict(list)
    for item in items:
        cat_name = item.get('category', 'Uncategorized')
        grouped[cat_name].append(item)
    return dict(sorted(grouped.items()))
