"""Rain belt data for the music team.
For each month: rain + snow (mm/h, month mean), averaged around the globe for each latitude row.
Run from the project folder:  python data/rain_belt_2000_2026/make_rain_belt_data.py
"""
import os, numpy as np, pandas as pd
DATA = "data"; OUT = os.path.join(DATA, "rain_belt_2000_2026"); os.makedirs(OUT, exist_ok=True)
R = 0.25; LAT = 90 - R / 2 - R * np.arange(720)          # row 0 = 89.875N ... row 719 = 89.875S
months = sorted(f[5:12] for f in os.listdir(os.path.join(DATA, "rain_monthly_npy")) if f.startswith("rain_") and f.endswith(".npy"))
rows = []
for ym in months:
    rain = np.load(os.path.join(DATA, "rain_monthly_npy", f"rain_{ym}.npy")).astype(np.float32)
    snow = np.load(os.path.join(DATA, "snow_monthly_npy", f"snow_{ym}.npy")).astype(np.float32)
    zonal = np.nanmean(rain + snow, axis=1)               # one value per latitude, mm/h
    np.save(os.path.join(OUT, f"rain_belt_{ym}.npy"), zonal.astype(np.float32))
    rows.append(zonal)
Z = np.stack(rows)                                         # [month, 720 latitudes]
np.save(os.path.join(OUT, "rain_belt_all_months.npy"), Z)
np.save(os.path.join(OUT, "latitudes.npy"), LAT.astype(np.float32))
# 17 bands of 5 degrees, 40S..40N (the notes in the music), mm/day
bands = np.arange(-40, 41, 5)
B = np.stack([Z[:, (LAT >= b - 2.5) & (LAT < b + 2.5)].mean(1) for b in bands], 1) * 24
df = pd.DataFrame(B, columns=[f"{b:+d}" for b in bands]); df.insert(0, "month", [m.replace("_", "-") for m in months])
trop = (LAT >= -30) & (LAT <= 30)
df["belt_centre_lat"] = [(LAT[trop] * z[trop] ** 2).sum() / (z[trop] ** 2).sum() for z in Z]
df.to_csv(os.path.join(OUT, "rain_belt_bands_mm_per_day.csv"), index=False, float_format="%.4f")
print(len(months), "months", Z.shape, "centre range", df.belt_centre_lat.min().round(1), df.belt_centre_lat.max().round(1))
