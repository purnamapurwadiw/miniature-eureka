# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: HomeInventory
def add_reminder(items, item_name, task_desc, due_date):
    """Добавить напоминание к элементу инвентаря."""
    new_item = {**items[item_name], "reminders": [{"task": task_desc, "due": due_date}]}
    items[item_name] = new_item
    print(f"Напоминание добавлено: '{item_name}' -> {task_desc} (до {due_date})")
