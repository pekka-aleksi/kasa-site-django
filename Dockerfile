FROM python:3.12.1-slim-bookworm
ENV PYTHONUNBUFFERED=1
WORKDIR /setup

RUN adduser --system --no-create-home django
####

RUN python -m pip install --upgrade pip
###
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
###
COPY start_script.sh start_script.sh
RUN chmod +x start_script.sh
###
COPY .my_pgpass .my_pgpass
COPY .pg_service.conf .pg_service.conf
COPY .env .env
COPY manage.py manage.py
COPY kasa_site_django kasa_site_django
#USER django
EXPOSE 8000
ENTRYPOINT ["./start_script.sh"]
