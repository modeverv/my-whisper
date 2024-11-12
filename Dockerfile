FROM ubuntu:22.04
#FROM nvidia/cuda:12.1.0-base-ubuntu22.04

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy scripts
COPY scripts/ ./scripts/
COPY src/ ./src/

# Make scripts executable
RUN chmod +x ./scripts/*.sh

# Set entry point
ENTRYPOINT ["./scripts/entrypoint.sh"]