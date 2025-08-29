# ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
# ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
# ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
# ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
# ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
# Copyright (c) 2025 Rıza Emre ARAS <r.emrearas@proton.me>
#
# Phantom Documentation Kit Docker Image
FROM python:3.11-slim

COPY requirements.txt /tmp/requirements.txt
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    # Required for Node.js repository
    ca-certificates curl gnupg \
    # Existing packages
    git \
    # Build tools for native modules
    build-essential python3 \
    # Sharp dependencies
    libvips42 libvips-dev \
    # Imagemin codec dependencies
    libjpeg-dev libpng-dev libwebp-dev libgif-dev libtiff-dev \
    # Additional build requirements
    pkg-config autoconf automake libtool nasm && \
    # Install Node.js 22.x LTS from official repository
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y nodejs && \
    # Verify installation
    node --version && npm --version && \
    # Clean up
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt