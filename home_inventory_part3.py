# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: HomeInventory
class Inventory:
    def __init__(self):
        self.rooms = {}
        self.items = []

    def add_item(self, name, room_name, category, warranty_months=0):
        if room_name not in self.rooms:
            self.rooms[room_name] = []
        item = {
            "name": name,
            "room": room_name,
            "category": category,
            "warranty_months": warranty_months,
            "added_at": __import__('datetime').datetime.now().isoformat()
        }
        self.items.append(item)
        self.rooms[room_name].append(item["name"])
        return item

    def get_items_by_room(self, room_name):
        return [item for item in self.items if item["room"] == room_name]

    def search_items(self, query):
        query_lower = query.lower()
        return [item for item in self.items if query_lower in item["name"].lower() or query_lower in item["category"].lower()]

inventory = Inventory()
