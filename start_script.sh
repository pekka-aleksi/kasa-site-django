#!/usr/bin/env bash

# run the django application with the 'runserver' command inside the Docker container


nginx

python manage.py makemigrations kasa_site_django
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput --username ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_EMAIL}
python manage.py runserver 0.0.0.0:8000
