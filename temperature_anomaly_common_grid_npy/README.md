# Temperature anomaly on the team's common grid (1880-01 -> 2025-12)

One file per month, same names as the original: `temperature_anomaly_YYYY_MM.npy`.

* Shape **720 x 1440** (was 90 x 180): the whole globe in pixels of 0.25 deg, the team's common grid.
  The same [row, column] is the same place in every dataset (precipitation, fires, lightning ...).
* **Row 0 = North (90N)**, row 719 = South. Note: the original files had row 0 = South; this is now flipped.
* **Column 0 = 180W**, column 1439 = 180E.
* Values: temperature anomaly in degrees C (float16). NaN = no data.
* Each original 2 deg value is copied into its 8 x 8 small pixels: the same values, nothing invented.
* Any place: row = int((90 - lat) / 0.25), column = int((lon + 180) / 0.25). Lausanne -> row 174, column 746.

    import numpy as np
    t = np.load("temperature_anomaly_2024_07.npy")   # 720 x 1440
    t[174, 746]                                      # Lausanne, July 2024 (about +2.6 C)

Check: the global (area-weighted) mean is about -0.2 C in 1880, +1.0 C in 2020, +1.2 C in 2025.
