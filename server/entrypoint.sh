#!/bin/sh
# Make migrations and migrate the database
echo "Making migrations and migrating the database."
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Execute the command passed to the Docker container (default is gunicorn)
exec "$@"
