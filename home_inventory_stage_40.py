# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: HomeInventory
import argparse

def main():
    parser = argparse.ArgumentParser(description="HomeInventory CLI")
    subparsers = parser.add_subparsers(dest="command")

    # add
    p_add = subparsers.add_parser("add", help="Add an item")
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--room", default="general")
    p_add.add_argument("--category", default="other")
    p_add.add_argument("--warranty", type=int, default=0)

    # list
    p_list = subparsers.add_parser("list", help="List items")

    # search
    p_search = subparsers.add_parser("search", help="Search items")
    p_search.add_argument("query")

    args = parser.parse_args()
    if args.command == "add":
        item = {"name": args.name, "room": args.room, "category": args.category, "warranty": args.warranty}
        items.append(item)
        print(f"Added: {args.name}")
    elif args.command == "list":
        for i in items:
            print(f"{i['name']} ({i['room']}, {i['category']})")
    elif args.command == "search":
        for i in items:
            if args.query.lower() in i["name"].lower():
                print(f"Found: {i['name']}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
