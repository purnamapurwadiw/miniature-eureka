# === Stage 45: Добавь восстановление из резервной копии ===
# Project: HomeInventory
def restore_from_backup(backup_file_path):
    """Восстанавливает данные из резервной копии, созданной функцией save_to_backup."""
    if not backup_file_path or not os.path.exists(backup_file_path):
        print("Резервная копия не найдена.")
        return False
    try:
        with open(backup_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        rooms = data.get("rooms", [])
        categories = data.get("categories", {})
        inventory = data.get("inventory", [])
        settings = data.get("settings", {})
        if rooms:
            Room.__init__(rooms)
        if categories:
            Category.__init__(categories)
        if inventory:
            InventoryItem.__init__(inventory)
        if settings:
            Settings.__init__(settings)
        print("Данные успешно восстановлены из резервной копии.")
        return True
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return False
