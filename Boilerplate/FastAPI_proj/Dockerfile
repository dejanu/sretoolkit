# Use slim Python image to reduce size
FROM python:3-alpine

WORKDIR /app

# bind mount instead since we don't need requirements
RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
    pip install --no-cache-dir -r  /tmp/requirements.txt

# Copy application code
COPY main.py /app/main.py

# Expose the port FastAPI will run on
EXPOSE 8000

# Fix the CMD path to match the actual file location
CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "8000", "--host", "0.0.0.0"]