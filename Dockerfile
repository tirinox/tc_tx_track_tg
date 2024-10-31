# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install gcc and other build tools
RUN apt-get update && \
    apt-get install -y gcc build-essential libgmp-dev && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Remove build tools to reduce image size
RUN apt-get purge -y --auto-remove build-essential

# Copy the current directory contents into the container at /app
# COPY . .

# Set PYTHONPATH to make imports work relative to the src directory
ENV PYTHONPATH=/app/src

# Define environment variable file location
ENV ENV_FILE_LOCATION=/app/.env

# Run the Python app
CMD ["python", "src/main.py"]
