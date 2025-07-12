FROM python:3.12-alpine AS build

WORKDIR /app
COPY /docs/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt