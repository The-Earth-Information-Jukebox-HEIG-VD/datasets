# Earth Information Jukebox: Datasets Container
# Lightweight Alpine image containing pre-processed NPY/NPZ climate data
# Used as an init container to populate data volumes
#
# Build with: docker build -t earth-jukebox-datasets .
# Usage: Run as init container to copy data to a shared volume

FROM alpine:latest

WORKDIR /datasets

# Copy all data files
COPY data/ .

# Default command explains usage
# In docker-compose, override with a copy command to populate volumes
CMD ["echo", "Data container - use as init container to populate volumes with: cp -r /datasets/. /data/"]
