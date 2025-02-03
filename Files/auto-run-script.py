# Автоматизация задач по расписанию (schedule)
"""
Можно запускать скрипты в определённое время.
Запуск скрипта каждый день в 12:00
"""
import schedule
import time

def task():
    print("Автоматическая задача выполнена!")

schedule.every().day.at("12:00").do(task)

while True:
    schedule.run_pending()
    time.sleep(60)
