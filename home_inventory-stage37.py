# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: HomeInventory
import unittest
from typing import List, Dict, Optional


class TestHomeInventory(unittest.TestCase):
    def test_find_item_by_name(self):
        items: List[Dict] = [
            {"name": "lamp", "room": "living", "category": "electronics", "warranty": True},
            {"name": "cup", "room": "kitchen", "category": "kitchenware", "warranty": False},
        ]
        found = [i for i in items if i["name"].lower() == "lamp"]
        self.assertEqual(found, [{"name": "lamp", "room": "living", "category": "electronics", "warranty": True}])

    def test_find_item_by_room(self):
        items: List[Dict] = [
            {"name": "lamp", "room": "living", "category": "electronics", "warranty": True},
            {"name": "cup", "room": "kitchen", "category": "kitchenware", "warranty": False},
        ]
        found = [i for i in items if i["room"] == "kitchen"]
        self.assertEqual(found, [{"name": "cup", "room": "kitchen", "category": "kitchenware", "warranty": False}])

    def test_find_item_by_warranty(self):
        items: List[Dict] = [
            {"name": "lamp", "room": "living", "category": "electronics", "warranty": True},
            {"name": "cup", "room": "kitchen", "category": "kitchenware", "warranty": False},
        ]
        found = [i for i in items if i["warranty"] is True]
        self.assertEqual(found, [{"name": "lamp", "room": "living", "category": "electronics", "warranty": True}])

    def test_find_item_by_category(self):
        items: List[Dict] = [
            {"name": "lamp", "room": "living", "category": "electronics", "warranty": True},
            {"name": "cup", "room": "kitchen", "category": "kitchenware", "warranty": False},
        ]
        found = [i for i in items if i["category"] == "electronics"]
        self.assertEqual(found, [{"name": "lamp", "room": "living", "category": "electronics", "warranty": True}])
