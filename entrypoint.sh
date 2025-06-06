#!/bin/bash
set -e

# Start Redis server in background
redis-server --daemonize yes

# Run Django migrations (optional)
python manage.py migrate

# Start Celery worker in background
celery -A meter_reading_manager worker --loglevel=info &

# Start Gunicorn to serve Django app (bind to 0.0.0.0:8000)
gunicorn octupus_test_project.wsgi:application --bind 0.0.0.0:8000
