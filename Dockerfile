FROM tiangolo/meinheld-gunicorn-flask:latest
RUN apt-get update -y
RUN pip install --upgrade pip
RUN pip install greenlet==3.0.0

LABEL org.opencontainers.image.title="Very basic sample web application"
LABEL org.opencontainers.image.authors="Mike Johnson (github.com/m-d-johnson)"
LABEL org.opencontainers.image.version="1.0.0"

COPY ./requirements.txt /app/app/requirements.txt
COPY ./app/main.py /app/app/main.py
COPY ./gunicorn_conf.py /app/gunicorn_config.py

WORKDIR /app

RUN pip install -r app/requirements.txt

# application folder
ENV APP_DIR /app

# expose web server port
EXPOSE 80

CMD ["gunicorn", "--conf", "gunicorn_config.py", "--bind", "0.0.0.0:80", "app.main:app"]
