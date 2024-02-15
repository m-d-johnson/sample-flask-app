# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

# https://docs.docker.com/engine/reference/builder/#from
FROM alpine:3.19.1

RUN apk add --no-cache python3 py3-pip
RUN rm -rf /usr/lib/python3.11/EXTERNALLY-MANAGED
# https://docs.docker.com/engine/reference/builder/#run
#RUN apt-get update -y
RUN python3 -m pip install --upgrade pip


# https://docs.docker.com/engine/reference/builder/#label
# https://specs.opencontainers.org/image-spec/annotations/#pre-defined-annotation-keys
LABEL org.opencontainers.image.title="Very basic sample web application"
LABEL org.opencontainers.image.authors="Mike Johnson (github.com/m-d-johnson)"
LABEL org.opencontainers.image.version="1.0.0"

# https://docs.docker.com/engine/reference/builder/#copy
COPY ./requirements.txt /app/requirements.txt
COPY ./app/main.py /app/sample-flask-app/main.py
COPY ./gunicorn_conf.py /app/gunicorn_config.py

# https://docs.docker.com/engine/reference/builder/#workdir
WORKDIR /app

# https://docs.docker.com/engine/reference/builder/#run
RUN pip install -r /app/requirements.txt

# Application Folder
# https://docs.docker.com/engine/reference/builder/#env
ENV APP_DIR /app

# Expose Web Server Port
# https://docs.docker.com/engine/reference/builder/#expose
EXPOSE 80

# https://docs.docker.com/engine/reference/builder/#cmd
CMD ["gunicorn", "--conf", "gunicorn_config.py", "--bind", "0.0.0.0:80", "sample-flask-app.main:app"]
