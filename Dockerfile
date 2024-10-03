FROM python:3.12-slim

# Set working directory
WORKDIR /app/backend

# Set environemnet variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN apt-get update \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .
