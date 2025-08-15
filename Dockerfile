FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ffmpeg ca-certificates gnupg && \
    rm -rf /var/lib/apt/lists/*

## Node.js install removed for python-only deployment. Add node install if needed.

# Set working directory
WORKDIR /app
COPY . /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Make start script executable
RUN chmod +x /app/start

# Start the app
CMD ["bash", "start"]
