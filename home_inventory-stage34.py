# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: HomeInventory
TEMPLATES = {
    "phone": {"name": "Телефон", "category": "Электроника", "warranty_months": 12},
    "laptop": {"name": "Ноутбук", "category": "Электроника", "warranty_months": 24},
    "kettle": {"name": "Чайник", "category": "Бытовая техника", "warranty_months": 6},
    "lamp": {"name": "Лампа", "category": "Освещение", "warranty_months": 3},
}

def apply_template(template_name, item):
    if template_name not in TEMPLATES:
        print(f"Нет шаблона '{template_name}'")
        return
    t = TEMPLATES[template_name]
    for field, value in t.items():
        setattr(item, field, value)

def quick_add(name, **kwargs):
    if "category" not in kwargs and "warranty_months" not in kwargs:
        print("Выберите шаблон или укажите category и warranty_months")
        return None
    item = Item(name=name)
    apply_template(kwargs.get("template"), item)
    for k, v in kwargs.items():
        if hasattr(item, k):
            setattr(item, k, v)
    return item

if __name__ == "__main__":
    i1 = quick_add("Samsung Galaxy S24", template="phone")
    print(i1)
    i2 = quick_add("Philips Hue", category="Освещение", warranty_months=2)
    print(i2)
