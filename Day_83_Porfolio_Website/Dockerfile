# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose the port Flask will run on
EXPOSE 8080

# Start Gunicorn with server:app
CMD ["gunicorn", "-b", "0.0.0.0:8080", "server:app"]
