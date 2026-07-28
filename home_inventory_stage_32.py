# === Stage 32: Добавь журнал действий пользователя ===
# Project: HomeInventory
class ActionLog:
    def __init__(self):
        self._log = []
    
    def add(self, action_type, description):
        entry = {"type": action_type, "description": description}
        self._log.append(entry)
        print(f"[LOG] {action_type}: {description}")

    @property
    def history(self):
        return list(self._log)
    
    def clear(self):
        self._log.clear()

def log_item_added(log, item_name):
    log.add("ITEM_ADDED", f"Item added: {item_name}")

def log_item_updated(log, item_name, field, old_val, new_val):
    log.add("ITEM_UPDATED", f"{item_name}.{field}: {old_val} -> {new_val}")

def log_room_added(log, room_name):
    log.add("ROOM_ADDED", f"Room added: {room_name}")

def log_search_performed(log, query):
    log.add("SEARCH", f"Search performed for: '{query}'")

actions = ActionLog()
log_item_added(actions, "Desk Lamp")
log_room_added(actions, "Kitchen")
