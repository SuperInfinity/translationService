# Base Image
FROM python:3.11-slim

# Working dir
WORKDIR /app

# Copy req and install'em
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Expose port, for FastAPI
EXPOSE 8000

# Run the app
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]