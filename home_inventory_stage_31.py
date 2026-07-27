# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: HomeInventory
def switch_profile():
    """Переключение активного профиля пользователя."""
    profiles = load_profiles()
    if not profiles:
        print("Нет сохранённых профилей.")
        return
    current = get_current_profile_name()
    for name, data in profiles.items():
        if name == current:
            print(f"Текущий профиль: {name}")
        else:
            print(f"[{name}] Имя: {data.get('name', 'Без имени')}, "
                  f"Комнаты: {len(data.get('rooms', []))}")
    choice = input("Введите имя профиля для переключения или Enter, чтобы остаться:\n> ").strip()
    if not choice:
        return
    target = find_profile_by_name(choice)
    if target is None:
        print(f"Профиль '{choice}' не найден.")
        return
    save_current_profile(target['name'])
    print(f"Переключение на профиль: {target['name']}")
