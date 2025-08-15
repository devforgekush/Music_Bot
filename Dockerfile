FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ffmpeg ca-certificates gnupg git libjpeg-dev zlib1g-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

## Node.js install removed for python-only deployment. Add node install if needed.


WORKDIR /app
COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y git ffmpeg && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set permissions and environment
RUN chmod +x Audify/__main__.py
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Railway runs on PORT environment variable
EXPOSE $PORT

# Start the bot
CMD ["python", "Audify/__main__.py"]
