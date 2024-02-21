# Use an official lightweight Python image.
# alpine is small, but if you need to compile dependencies, consider using slim
FROM python:3.11.5-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
# This ensures that the packages are up to date and that any required dependencies are present
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /usr/src/app

# Install Python dependencies
# Copy the requirements file first to cache the Docker layer and install the requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
# Copy the rest of your application code afterwards to avoid cache invalidation from other file changes
COPY . .

# Add a user to run the application
# Running as root is a bad practice, so we create a user with no password
# with a home directory and switch to it.
RUN addgroup --system app && adduser --system --group app
USER app

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]