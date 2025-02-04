FROM python:3.10.4-slim-bullseye

# Env variables

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# working directory
WORKDIR /code

COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .