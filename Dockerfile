# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Define environment variable to prevent Python from buffering output
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "Flask.py"]

