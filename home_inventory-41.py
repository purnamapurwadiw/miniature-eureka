# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: HomeInventory
def dry_run(operation, payload):
    """Simulate a write operation without persisting it, returning a dry-run report."""
    import datetime
    return {
        "mode": "dry-run",
        "operation": operation,
        "payload": payload,
        "timestamp": datetime.datetime.now().isoformat(),
        "status": "simulated",
        "note": "No changes were made to any storage."
    }
