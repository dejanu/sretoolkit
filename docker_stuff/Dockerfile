## used for remote build: docker build -t test https://github.com/dejanu/sretoolkit.git#remotebuild:docker_stuff --no-cache
# Python runtime as a parent image
FROM python:slim-bullseye

# MAINTAINER (deprecated)
LABEL org.dejanualex.image.authors="dejanualex"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY test.py /app

# Run app.py when the container launches
CMD ["python", "test.py"]