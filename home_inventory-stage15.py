# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: HomeInventory
def calculate_weekly_stats(items):
    from datetime import date, timedelta
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    stats = {}
    for item in items:
        if 'purchase_date' not in item or not isinstance(item['purchase_date'], str):
            continue
        try:
            purchase_date = date.fromisoformat(item['purchase_date'])
            week_delta = (purchase_date - week_start).days // 7
            key = f"Week {week_delta}" if week_delta != 0 else "Current Week"
            stats[key] = stats.get(key, 0) + 1
        except ValueError:
            continue
    return stats
