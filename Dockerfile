# Use an official lightweight Python image.
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Install system libraries required by pandas and numpy
RUN apt-get update && apt-get install -y \
    libatlas-base-dev gfortran

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run the application
CMD ["gunicorn", "flask_app:app", "--bind", "0.0.0.0:8080"]
