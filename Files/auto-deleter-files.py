# Автоматическая очистка ненужных файлов
# Можно удалять временные файлы или кеш.

# Удаление файлов старше 7 дней
import os
import time

folder = "logs"
now = time.time()

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.stat(filepath).st_mtime < now - 7 * 86400:
        os.remove(filepath)