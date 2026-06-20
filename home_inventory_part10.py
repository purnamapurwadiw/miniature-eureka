# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: HomeInventory
def export_to_json():
    import json
    data = {
        "rooms": rooms,
        "categories": categories,
        "items": items,
        "metadata": {"version": 10, "timestamp": datetime.now().isoformat()}
    }
    return json.dumps(data, indent=2, ensure_ascii=False)
