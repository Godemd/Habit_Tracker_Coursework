#!/bin/bash

python manage.py migrate
python manage.py collectstatic --no-input
gunicorn habits_project.wsgi:application --bind 0.0.0.0:8000 