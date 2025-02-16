FROM python:3.9-slim

LABEL authors="Arslon"

WORKDIR /app

COPY "flask_docker/requirements.txt" .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "flask_docker/server.py"]