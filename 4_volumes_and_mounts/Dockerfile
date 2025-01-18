FROM python:3.12.3-slim

WORKDIR /app

# Copy only requirements first for caching
COPY app/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt