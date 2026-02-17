FROM python:3.12-slim

WORKDIR /quasimoto

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt

