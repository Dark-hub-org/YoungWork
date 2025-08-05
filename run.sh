#!/bin/bash
echo "Waiting for PostgreSQL..."

while ! timeout 1 bash -c "echo > /dev/tcp/db/5432"; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
daphne -b 0.0.0.0 -p 8000 backend.asgi:application