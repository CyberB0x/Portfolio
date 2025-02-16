# Используем офицальную образ Python
FROM python:3.9-slim

# Указываем рабочую дерикторию в контейнере
WORKDIR /app

# Копируем приложение в контейнер
COPY "hello_docker/main.py" .

# Запускаем приложение
CMD ["python", "main.py"]
