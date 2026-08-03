# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: HomeInventory
# Integrity check and repair for HomeInventory
def integrity_check_and_repair():
    """Check data consistency and fix simple issues."""
    errors = []
    
    # Check that all items have required fields
    for item in inventory:
        if not hasattr(item, 'name') or not item.name:
            errors.append(f"Item missing name: {item}")
            continue
        if not hasattr(item, 'category') or not item.category:
            item.category = "Uncategorized"
            errors.append(f"Fixed category for {item.name}")
        
        # Check that quantity is valid
        if hasattr(item, 'quantity') and item.quantity < 0:
            item.quantity = 0
            errors.append(f"Fixed negative quantity for {item.name}: set to 0")

    # Check rooms reference existing categories
    valid_categories = set(cat.name for cat in categories)
    for room in rooms:
        if hasattr(room, 'category') and room.category not in valid_categories:
            room.category = "General"
            errors.append(f"Fixed invalid category for room {room.name}: set to General")

    return errors
