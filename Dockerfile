FROM nikolaik/python-nodejs:python3.10-nodejs19

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ffmpeg ca-certificates gnupg && \
    rm -rf /var/lib/apt/lists/*

# Install Node 18 via NVM and make it persistent
ENV NVM_DIR=/root/.nvm
ENV NODE_VERSION=18
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && \
    . "$NVM_DIR/nvm.sh" && \
    nvm install $NODE_VERSION && \
    nvm alias default $NODE_VERSION && \
    nvm use default && \
    npm install -g npm
ENV PATH=$NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# Set working directory
WORKDIR /app
COPY . /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Make start script executable
RUN chmod +x /app/start

# Start the app
CMD ["bash", "start"]
