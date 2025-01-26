#!/bin/bash

# Выход при ошибке любой команды
set -e

# Применяем миграции
echo "Applying migrations..."
poetry run python manage.py migrate

# Сбор статических файлов
echo "Collecting static files..."
poetry run python manage.py collectstatic --noinput