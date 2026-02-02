FROM python:3.10-slim

WORKDIR /app

# Install build dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . /app

EXPOSE 8000

# Use PORT env var if provided by host, else default to 8000
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]
