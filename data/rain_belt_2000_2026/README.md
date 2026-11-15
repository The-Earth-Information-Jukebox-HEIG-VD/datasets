# Rain belt 2000–2026 (data behind "The rain belt swings with the seasons")

For every month, rain + snow from NASA GPM IMERG, averaged **around the globe for each latitude**
(all longitudes, land and ocean). The longitudes disappear and the latitudes stay.

## Files

| File | Shape | Unit | What it is |
|---|---|---|---|
| `rain_belt_YYYY_MM.npy` | (720,) | mm/h | one month: one value per latitude row, same rows as our common grid |
| `rain_belt_all_months.npy` | (318, 720) | mm/h | all months together, row 0 = June 2000 |
| `latitudes.npy` | (720,) | degrees | latitude of each value: index 0 = 89.875°N, index 719 = 89.875°S |
| `rain_belt_bands_mm_per_day.csv` | 318 rows | mm/day | 17 bands of 5° from 40°S to 40°N (the 17 notes in our music), plus `belt_centre_lat` |

- Index `i` ↔ latitude `90 − 0.125 − 0.25 × i` (north first, like all our files).
- mm/h × 24 = mm/day.
- `belt_centre_lat` = where the rain is strongest between 30°S and 30°N (rain² weighted). It moves north in July and south in January.
- Period: June 2000 – November 2026 (November 2026 is a partial month, 13 days).

Made with `make_rain_belt_data.py` from the monthly files in `rain_monthly_npy` and `snow_monthly_npy`.
