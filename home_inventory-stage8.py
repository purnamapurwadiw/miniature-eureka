# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: HomeInventory
import sys, os, json, re
from datetime import datetime

def show_menu():
    print("\n=== HomeInventory Menu ===")
    print("1. Add Item (Room|Category|Name|Warranty)")
    print("2. Search Items (Keyword)")
    print("3. List All Items")
    print("4. Exit")
    try:
        choice = input("Select option [1-4]: ").strip()
        return choice
    except EOFError:
        sys.exit(0)

def add_item():
    room = input("Room (e.g., Kitchen): ").title() or "General"
    category = input("Category (e.g., Electronics): ").title() or "Uncategorized"
    name = input("Item Name: ")
    if not name: return False
    warranty_months = input("Warranty in months (0=none): ").strip()
    try:
        w = int(warranty_months)
    except ValueError:
        w = 0
    expiry = datetime.now().month + w // 30, datetime.now().day if w % 30 else None # Simplified logic for demo
    item = {"room": room, "category": category, "name": name, "warranty_months": w}
    items.append(item)
    print(f"Added: {item['name']} in {room}")
    return True

def search_items(keyword):
    matches = [i for i in items if keyword.lower() in i.get("name", "").lower() or 
               keyword.lower() in i.get("category", "").lower() or 
               keyword.lower() in i.get("room", "").lower()]
    print(f"\nFound {len(matches)} item(s):")
    for m in matches:
        print(f"  - [{m['room']}] {m['name']} ({m['category']}) [Warranty: {m['warranty_months']}mo]")

def list_all():
    if not items:
        print("No items found.")
        return
    for i, item in enumerate(items, 1):
        w = item.get('warranty_months', 0)
        exp_str = "Expired" if w > 0 and datetime.now().month + (w//30) < datetime.now().month else f"{w}mo left"
        print(f"{i}. [{item['room']}] {item['name']} ({item['category']}) - Warranty: {exp_str}")

items = []
while True:
    choice = show_menu()
    if choice == "1": add_item()
    elif choice == "2": search_items(input("Enter keyword: ").strip())
    elif choice == "3": list_all()
    elif choice == "4" or not choice: break
