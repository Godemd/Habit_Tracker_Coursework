# Установите базовый образ
FROM python:3.12-slim

# Установите зависимости для сборки
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установите Poetry
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s "${HOME}/.local/bin/poetry" /usr/local/bin/poetry

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы зависимостей
COPY pyproject.toml poetry.lock ./

# Установите зависимости
RUN poetry install --no-root

# Скопируйте исходный код
COPY . .

COPY docker-entrypoint.sh /usr/local/bin/

# Настройка порта для приложения
EXPOSE 8000

RUN chmod +x /usr/local/bin/docker-entrypoint.sh