# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: HomeInventory
class TagManager:
    def __init__(self, items_db):
        self.items_db = items_db
        self.tags_db = {}  # {tag_name: set(item_ids)}

    def add_tag(self, item_id, tag_name):
        if not self._validate_item_id(item_id):
            return False
        if tag_name in self.tags_db:
            self.tags_db[tag_name].add(item_id)
        else:
            self.tags_db[tag_name] = {item_id}
        self.items_db[item_id]['tags'].append(tag_name)
        return True

    def remove_tag(self, item_id, tag_name):
        if not self._validate_item_id(item_id):
            return False
        if tag_name in self.tags_db and item_id in self.tags_db[tag_name]:
            self.tags_db[tag_name].discard(item_id)
            self.items_db[item_id]['tags'] = [t for t in self.items_db[item_id]['tags'] if t != tag_name]
            return True
        return False

    def _validate_item_id(self, item_id):
        return isinstance(item_id, int) and 0 <= item_id < len(self.items_db)
