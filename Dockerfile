# Базовый образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY app.py .

# Переменные окружения
ENV ENV=production
ENV PORT=5000

# Открываем порт
EXPOSE 5000

# Команда запуска
CMD ["python", "app.py"]
