FROM python:3.10-slim


# Рабочая директория
WORKDIR /app


# Установка Python зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Копируем код
COPY . .

ENV PYTHONPATH=/app

RUN mkdir -p /app/logs

# Установка прав для отчетов allure
RUN mkdir -p /app/allure-results && chmod -R 777 /app/allure-results

# Запуск тестов

ENTRYPOINT ["python", "-m", "pytest"]
CMD ["-n", "1"]
