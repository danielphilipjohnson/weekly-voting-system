FROM python:3.9-slim as production
LABEL maintainer="daniel-philip-johnson.com"

ENV PYTHONUNBUFFERED 1

COPY requirements/prod.txt ./requirements/prod.txt
COPY ./app ./app

WORKDIR /app
EXPOSE 8088

RUN pip install -r /requirements/prod.txt