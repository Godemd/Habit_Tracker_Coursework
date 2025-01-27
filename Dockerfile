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
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry
ENV POETRY_VERSION=2.0.1
RUN curl -sSL https://install.python-poetry.org -o install-poetry.py && \
    python3 install-poetry.py --version $POETRY_VERSION && \
    ln -s "${HOME}/.local/bin/poetry" /usr/local/bin/poetry

# Проверка версии Poetry
RUN poetry --version

# Установка зависимостей проекта
RUN poetry install --no-root