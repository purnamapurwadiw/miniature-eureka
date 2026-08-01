# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: HomeInventory
def get_recommendations(self):
        """Рекомендации следующего действия на основе текущего состояния."""
        rec = []
        
        # Если нет комнат, предлагаём создать первую комнату
        if not self.rooms:
            rec.append("Создайте первую комнату (например 'Кухня'), чтобы начать каталогизацию.")
            return rec
        
        # Если в комнате есть предметы без гарантии — предложим добавить
        for room in self.rooms.values():
            items_without_warranty = [i for i in room.items if not i.warranty]
            if items_without_warranty:
                rec.append(f"Добавьте гарантию для {len(items_without_warranty)} предметов в комнате '{room.name}'.")
        
        # Если есть предметы без категории — предложим присвоить
        for room in self.rooms.values():
            items_without_category = [i for i in room.items if not i.category]
            if items_without_category:
                rec.append(f"Присвойте категорию {len(items_without_category)} предметам в комнате '{room.name}'.")
        
        # Если есть предметы без оценок — предложим оценить
        for room in self.rooms.values():
            items_without_rating = [i for i in room.items if not i.rating]
            if items_without_rating:
                rec.append(f"Оцените {len(items_without_rating)} предметов в комнате '{room.name}' для приоритизации.")
        
        # Если нет поисковых запросов — предложим поиск
        if not self.search_history:
            rec.append("Попробуйте поискать предметы по названию или категории, чтобы быстро найти нужное.")
        
        return rec if rec else ["Проект развивается корректно. Добавьте новые вещи в любую комнату."]
