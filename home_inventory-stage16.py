# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: HomeInventory
def calculate_monthly_statistics(items):
    from datetime import datetime, timedelta
    
    stats = {}
    for item in items:
        if not item.get('purchase_date'):
            continue
        try:
            date_obj = datetime.strptime(item['purchase_date'], '%Y-%m-%d')
            month_key = f"{date_obj.year}-{date_obj.month:02d}"
            stats[month_key] = stats.get(month_key, 0) + 1
        except ValueError:
            continue
    
    return sorted(stats.items())
