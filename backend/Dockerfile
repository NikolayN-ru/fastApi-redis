FROM python:3.8

RUN apt-get update && pip install --upgrade pip
RUN python -m pip install fastapi gunicorn uvicorn uvloop httptools aioredis hiredis asgi_redis pydantic

WORKDIR /app

ADD . .