# Установите базовый образ
FROM python:3.12-slim

# Установите рабочую директорию
WORKDIR /app

# Скопируйте исходный код
COPY . /app

# Установите зависимости для сборки
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установите Poetry и зависимости
ENV POETRY_VERSION=1.8.3
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s "${HOME}/.local/bin/poetry" /usr/local/bin/poetry && \
    poetry install --no-root

COPY docker-entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Настройка порта для приложения
EXPOSE 8000

# Команда для запуска приложения
CMD ["poetry", "run", "gunicorn", "habits_project.wsgi:application", "--bind", "0.0.0.0:8000"]