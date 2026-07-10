# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: HomeInventory
def check_expired_reminders():
    """Проверяет просроченные напоминания о гарантиях."""
    expired = []
    for item in inventory:
        if item.warranty and item.warranty.expiry_date:
            if datetime.now() > item.warranty.expiry_date:
                expired.append(item)
                print(f"⚠️ Гарантия истекла для: {item.name}")
    return expired

expired_items = check_expired_reminders()
if expired_items:
    print(f"\nВсего просроченных гарантий: {len(expired_items)}")
