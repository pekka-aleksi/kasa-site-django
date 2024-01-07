#!/usr/bin/env bash

# run the django application with the 'runserver' command inside the Docker container

python manage.py makemigrations kasa_site_django
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
