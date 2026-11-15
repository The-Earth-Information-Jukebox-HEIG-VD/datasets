# Earth Information Jukebox - Datasets

Pre-processed NASA Earth data for the sonification backend.

## Data Format

`data/` holds one subfolder per dataset. Each file is a NumPy `.npy` array (no `.npz` or `.json`), one file per month (per year for night lights). All maps are 720 x 1440 (0.25 degree pixels).

| Folder | Period (first - last file) | File pattern | Shape / dtype |
|---|---|---|---|
| `co2_2002_2022/` | 2002-09 - 2022-03 (235 files) | `co2_YYYY_MM.npy` | 720 x 1440, float32 |
| `fires_2002_2026/` | 2002-07 - 2026-11 (293 files) | `fires_YYYY_MM.npy` | 720 x 1440, float16 |
| `lightning_2017_2023/` | 2017-03 - 2023-07 (77 files) | `lightning_YYYY_MM.npy` | 720 x 1440, float16 |
| `nightlights_2012_2023/` | 2012 - 2023 (12 files, one per year) | `nightlights_YYYY.npy` | 720 x 1440, float32 |
| `precipitation_rain_2000_2026/` | 2000-06 - 2026-11 (318 files) | `rain_YYYY_MM.npy` | 720 x 1440, float16 |
| `precipitation_snow_2000_2026/` | 2000-06 - 2026-11 (318 files) | `snow_YYYY_MM.npy` | 720 x 1440, float16 |
| `temperature_anomaly_1880_2025/` | 1880-01 - 2025-12 (1752 files) | `temperature_anomaly_YYYY_MM.npy` | 720 x 1440, float16 |

Shape and dtype were read from the first and last file of each folder. Only `temperature_anomaly_1880_2025/` has its own `README.md` (grid orientation, how to index a place).

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

Data is derived from NASA sources:
- GISTEMP - Global Surface Temperature Analysis (temperature anomaly)
- GPM IMERG - rain and snow
- MODIS active fires
- ISS LIS - lightning
- NASA SVS 5276 - Earth at Night (night lights)
- CO2 maps processed by the team

See the `data_processing` repository for some of the processing scripts (`nightlights/`, `temperature_anomaly/`, `precipitation/`, `common_grid/`).

## CI

`.github/workflows/docker-publish.yml` builds and pushes the image to GitHub Container Registry (`ghcr.io`) **only when a `v*` tag is pushed** (e.g. `v1.0.0`). Image tags: `1.0.0`, `1.0` and `latest`. Because `data/` is about 6.3 GB, the workflow first frees runner disk space (removes preinstalled SDKs such as .NET and Android, prunes Docker images) and deletes `.git` (a ~1.3 GB pack the image does not use) before building with Buildx.
