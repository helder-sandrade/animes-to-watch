#!/bin/sh

# end if script error
set -e

while ! nc -z $DBHOST $DBPORT; do
  echo "Esperando MySQL"
  sleep 2
done

echo "MySQL OK"

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
gunicorn animes.wsgi --bind 0.0.0.0:80
#python manage.py runserver 0.0.0.0:8000