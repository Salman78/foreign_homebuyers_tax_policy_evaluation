# Use an official lightweight Python image as the base
FROM python:3.10-slim

# Set environment variables to avoid buffer issues and ensure UTF-8 encoding
ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Set the working directory inside the container
WORKDIR /app

# Copy the project requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Install PostgreSQL client to interact with the PostgreSQL database
RUN apt-get update && apt-get install -y postgresql-client && apt-get clean

# Expose a port if your app has a web UI (optional, e.g., Flask/Django)
EXPOSE 8000

# Specify the command to run the application
CMD ["python", "scrape.py"]
