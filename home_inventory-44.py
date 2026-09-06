# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: HomeInventory
import shutil, os, datetime

def backup_data_file(data_file_path):
    """Создаёт резервную копию файла данных с расширением .bak и указывающим датой."""
    if not os.path.exists(data_file_path):
        return
    backup_path = f"{data_file_path}.{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
    shutil.copy2(data_file_path, backup_path)
