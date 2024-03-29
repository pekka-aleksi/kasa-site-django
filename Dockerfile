FROM python:3.12.1-slim-bookworm

ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_EMAIL
ARG DJANGO_SUPERUSER_PASSWORD

ENV DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME
ENV DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL
ENV DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD

ENV PYTHONUNBUFFERED=1
WORKDIR /setup

#RUN useradd --create-home --system django

COPY start_script.sh start_script.sh
RUN chmod +x start_script.sh

#USER django
####

RUN python -m pip install --upgrade pip
###

COPY requirements.txt requirements.txt
RUN python -m pip install --user -r requirements.txt
###

COPY .env .env
COPY manage.py manage.py
COPY kasa_site_django kasa_site_django

RUN apt-get update && apt-get install -y nginx

######
COPY .nginx/nginx.conf /etc/nginx/conf.d/default.conf
RUN rm -rf /usr/share/nginx/html

EXPOSE 8312
# we expose NGINX port
ENTRYPOINT ["./start_script.sh"]
