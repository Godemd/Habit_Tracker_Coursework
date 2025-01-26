#!/bin/bash

# Выход 
set -e

# Применяем миграции
echo "Applying migrations..."
poetry run python manage.py migrate

# Сбор статических файлов
echo "Collecting static files..."
poetry run python manage.py collectstatic --noinput

echo "Starting server..."
poetry run gunicorn habits_project.wsgi:application --bind 0.0.0.0:8000