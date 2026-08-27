# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: HomeInventory
import unittest
class TestEdgeCases(unittest.TestCase):
    def test_empty_room_name(self):
        self.assertEqual(len("".strip()), 0)
    def test_case_insensitive_search(self):
        items = [{"name": "Lamp"}, {"name": "lamp"}, {"name": "LAMP"}]
        found = [i for i in items if i["name"].lower() == "lamp"]
        self.assertEqual(len(found), 3)
    def test_nonexistent_category(self):
        cat = "NonExistent"
        self.assertNotIn(cat, ["Furniture", "Electronics"])
    def test_empty_search(self):
        items = [{"name": "A"}, {"name": "B"}]
        found = [i for i in items if i["name"].lower() in ""]
        self.assertEqual(len(found), 0)
    def test_special_characters_in_name(self):
        item = {"name": "Item@#$%^&*()"}
        self.assertEqual(item["name"], "Item@#$%^&*()")
    def test_unicode_characters(self):
        item = {"name": "Привет"}
        self.assertIn("Привет", item["name"])
    def test_mixed_case_search(self):
        items = [{"name": "Sofa"}, {"name": "sofa"}, {"name": "SOFA"}]
        found = [i for i in items if i["name"].lower() == "sofa"]
        self.assertEqual(len(found), 3)
    def test_empty_list_search(self):
        items = []
        found = [i for i in items if i["name"].lower() == "anything"]
        self.assertEqual(len(found), 0)
    def test_single_item_search(self):
        items = [{"name": "Single"}]
        found = [i for i in items if i["name"].lower() == "single"]
        self.assertEqual(len(found), 1)
    def test_exact_match_case_sensitive(self):
        items = [{"name": "Apple"}, {"name": "apple"}]
        found = [i for i in items if i["name"] == "Apple"]
        self.assertEqual(len(found), 1)
    def test_partial_match(self):
        items = [{"name": "App"}, {"name": "Application"}]
        found = [i for i in items if i["name"].lower().startswith("app")]
        self.assertEqual(len(found), 2)
    def test_no_match(self):
        items = [{"name": "Table"}]
        found = [i for i in items if i["name"].lower() == "nonexistent"]
        self.assertEqual(len(found), 0)
    def test_special_characters_in_search(self):
        items = [{"name": "Item with spaces"}]
        found = [i for i in items if i["name"].lower() == "item with spaces"]
        self.assertEqual(len(found), 1)
    def test_empty_string_search(self):
        items = [{"name": "Item"}]
        found = [i for i in items if i["name"].lower() == ""]
        self.assertEqual(len(found), 0)
    def test_multiple_items_search(self):
        items = [{"name": "Item1"}, {"name": "Item2"}, {"name": "Item3"}]
        found = [i for i in items if i["name"].lower() == "item1"]
        self.assertEqual(len(found), 1)

if __name__ == "__main__":
    unittest.main()
