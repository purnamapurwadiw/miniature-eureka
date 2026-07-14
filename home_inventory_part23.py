# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: HomeInventory
import textwrap, sys

def print_inventory_table(items):
    if not items:
        print("Каталог пуст.")
        return
    headers = ["ID", "Название", "Комната", "Категория", "Гарантия"]
    widths = [len(h) for h in headers]
    for item in items:
        row = []
        for h in headers:
            val = getattr(item, h.lower(), "")
            if isinstance(val, list):
                val = ", ".join(str(v) for v in val)
            row.append(str(val))
            widths[headers.index(h)] = max(widths[headers.index(h)], len(row[-1]))
    line = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    print(line)
    header_line = "|" + "|".join(textwrap.fill(str(h).ljust(w), w) for h, w in zip(headers, widths)) + "|"
    print(header_line)
    print(line)
    for item in items:
        row = []
        for h in headers:
            val = getattr(item, h.lower(), "")
            if isinstance(val, list):
                val = ", ".join(str(v) for v in val)
            row.append(textwrap.fill(str(val).ljust(w), w))
        print("|" + "|".join(row) + "|")
    print(line)

if __name__ == "__main__":
    print_inventory_table([])  # демонстрация: пустой каталог
