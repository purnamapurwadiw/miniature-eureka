# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: HomeInventory
def undo_last(self):
        if not self.history:
            return None
        action = self.history.pop()
        if isinstance(action, ("add_item", "remove_item")):
            item_id, room_id = action
            if item_id in self.items:
                del self.items[item_id]
                return {"success": True, "message": "Item restored to inventory."}
            elif item_id not in self.items and action[0] == "add_item":
                self.items[item_id] = Item(
                    name=action[1]["name"], category=action[1].get("category"),
                    condition=action[1].get("condition", "new"), warranty=action[1].get("warranty", 0),
                    room_id=room_id, purchase_date=action[1].get("purchase_date")
                )
                return {"success": True, "message": "Item added back."}
            else:
                return {"success": False, "message": "Cannot restore item in this state."}
        elif isinstance(action, ("add_room", "remove_room")):
            room_id = action[0] if action[0] == "add_room" else action[1]
            if room_id in self.rooms:
                del self.rooms[room_id]
                return {"success": True, "message": f"Room {room_id} restored."}
        return {"success": False, "message": "No reversible action to undo."}
