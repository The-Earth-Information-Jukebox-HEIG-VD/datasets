# Earth Information Jukebox - Datasets

Pre-processed NASA Earth data for the sonification backend.

## Data Format

Place processed dataset files in the `data/` directory:

- `*.npz` - NumPy compressed arrays with intensity maps
- `*.npy` - NumPy arrays with time series data
- `*.json` - Metadata files describing datasets

## Docker Image

This repository builds a lightweight Alpine-based Docker image containing the data files. The image is used as an init container to populate shared volumes.

### Building

```bash
docker build -t earth-jukebox-datasets .
```

### Usage in Docker Compose

```yaml
services:
  data-init:
    image: ghcr.io/the-earth-information-jukebox-heig-vd/datasets:latest
    volumes:
      - jukebox-data:/data
    command: >
      sh -c "if [ ! -f /data/.initialized ]; then
        cp -r /datasets/. /data/ && touch /data/.initialized;
      fi"
```

## Data Sources

Data is derived from NASA's Earth Information Center:
- GISTEMP - Global Surface Temperature Analysis
- POWER - Prediction Of Worldwide Energy Resources
- SVS - Scientific Visualization Studio assets

See the main project documentation for data processing scripts.
