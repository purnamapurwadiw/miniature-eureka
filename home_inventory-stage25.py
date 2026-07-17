# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: HomeInventory
def parse_date(date_str):
    """Парсит дату в формате ДД.ММ.ГГГГ, возвращает datetime.date или None."""
    try:
        parts = date_str.strip().split('.')
        if len(parts) != 3:
            return None
        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        from datetime import date
        return date(year, month, day)
    except (ValueError, TypeError):
        return None

def format_date(date_obj):
    """Форматирует date в ДД.ММ.ГГГГ."""
    if date_obj is None:
        return ''
    return f'{date_obj.day}.{date_obj.month}.{date_obj.year}'

def show_error(message, title='Ошибка'):
    """Выводит стилизованное сообщение об ошибке."""
    print(f'\n{"="*40}')
    print(f'  {title}')
    print(f'  {message}')
    print(f'{"="*40}\n')

def show_success(message):
    """Выводит успешное действие."""
    print(f'\n✓ {message}\n')
