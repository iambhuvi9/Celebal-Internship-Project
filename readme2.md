# 🧠 Machine Learning Pipeline

```text
Smart Meter Logs + Weather History + Holiday Schedules + Demographic Categories
                                         │
                                         ▼
                             Data Cleaning & Merge
                   (Joined on Date Keys and Household LCLid)
                                         │
                                         ▼
                            Feature Engineering Module
            (Temporal Extractions • 1D & 7D Lags • 3D Rolling Averages)
                                         │
                                         ▼
                       LightGBM Optimization Engine Training
                (Early Stopping Evaluation Loop • 12‑Feature Space)
                                         │
                                         ▼
                            Serialized Model Artifact
                          (energy_forecast_model.pkl)
                                         │
                                         ▼
                         Streamlit Reactive GUI Execution
          (Interactive Telemetry Processing & Automated Control Actions)
---

---text

# Data Engineering Specifications

Input Features Matrix (12 Explicit Vectors)
temperatureMax – Daily maximum temperature (°C).

temperatureMin – Daily minimum temperature (°C).

humidity – Mean relative humidity fraction.

windSpeed – Wind velocity (mph).

Month – Integer (1–12) representing seasonal variation.

Day_of_Week – Integer (0–6) for weekday cycles.

Is_Weekend – Binary flag (0/1) for weekend detection.

is_bank_holiday – Binary flag (0/1) for holiday shifts.

acorn_encoded – Encoded socio‑economic household profile.

energy_lag_1 – Energy usage from 1 day prior (kWh).

energy_lag_7 – Energy usage from 7 days prior (kWh).

energy_rolling_mean_3 – 3‑day rolling average load (kWh).
### Prediction Target

***`energy_sum`**: Continuous absolute daily electricity consumption volume measured in Kilowatt-hours (`kWh`).
