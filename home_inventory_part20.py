# === Stage 20: Добавь восстановление записей из архива ===
# Project: HomeInventory
def restore_from_archive(self, path):
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or line == '---':
                    continue
                parts = line.split(',', 4)
                if len(parts) < 5:
                    print(f"Warning: Skipping malformed line: {line}")
                    continue
                item_id, name, room, category, warranty = parts
                self.items[item_id.strip()] = {
                    'id': item_id.strip(),
                    'name': name.strip(),
                    'room': room.strip(),
                    'category': category.strip(),
                    'warranty_months': int(warranty.strip()),
                    'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M'),
                }
        print(f"Restored {len(self.items)} items from archive.")
