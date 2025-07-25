# Use a small Python base image
FROM python:3.12-slim

# Set a working directory
WORKDIR /app

# Install system dependencies for pip, requests, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . /app

# Set environment variables for Flask
ENV FLASK_APP=brevity
ENV FLASK_ENV=production
ENV OLLAMA_HOST=http://ollama:11434

# Expose the Flask port
EXPOSE 5000

#  Run the app with Gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "brevity:create_app()"]
