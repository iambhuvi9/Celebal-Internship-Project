# Autonomous Energy Optimization Platform for Smart Grids

A production-grade, modular energy analytics and predictive forecasting system built using Python, Scikit-Learn, Streamlit, and Plotly. The platform ingests large-scale smart meter telemetry data alongside historical hourly weather streams to forecast consumption, isolate dynamic usage patterns, and dispatch automated demand-side optimization directives in real-time.

The core architecture leverages advanced ensemble machine learning (Random Forest Regression) to map non-linear thermal sensitivities and temporal variations across the grid. By synthesizing meteorological factors with temporal modifiers, the platform generates high-fidelity demand profiles and actionable optimization indexes without requiring complex local hardware integration.

---

## Features

- **High-Scale Ingestion Pipeline**: Built to efficiently process large-scale smart meter arrays (optimized via chunk-based low-memory configurations) alongside dense, multi-variable historical weather streams.
- **Granular Temporal Feature Suite**: Extracts deep cyclical attributes from raw date stamps (including Month indices, Day-of-Week sequences, and binary Weekend indicators) to isolate commercial shutdowns and residential load shifts.
- **Ensemble Predictive Core**: Utilizes a highly trained Random Forest Regressor framework to map multi-spectral weather variations and structural calendar markers against localized volumetric demand profiles (`energy_sum`).
- **Real-Time Automated Dispatch Engine**: An algorithmic rule-base that parses ambient temperatures, kinetic wind draft patterns, and moisture indices to spin up instantaneous grid efficiency badges and localized HVAC optimization overrides.
- **Enterprise SaaS Dashboard**: Deploys an interactive, premium Single Page Application UI via Streamlit featuring unified digital control selectors, master toggle overrides, and dynamic Plotly spline area graphs.

---

## 🖼️ Project Previews & Visual Analytics

### 1. Enterprise Control Center & Core Forecasting Interface
The central data orchestration center managed via Streamlit, tracking real-time telemetry matrices, master temporal toggles, and multi-metric executive KPI rows.

<img src="assets/Dashboard Platform.png" alt="Enterprise Energy Dashboard Interface" width="100%" />

---

### 2. Multi-Variable Telemetry Simulation Matrix
Sample interactive configuration showing the input simulation panel where min/max thermal limits, relative humidity vectors, and calendar schedules are manipulated to stress-test grid behaviors.

<img src="assets/Telemetry Input.png" alt="Telemetry Simulation Matrix Interface" width="100%" />

---

### 3. Predictive 7-Day Demand Matrix (Plotly Spline Area)
High-end analytical visualization displaying the forecasted weekly energy load curve, generating precise cyclic sequence projections based on user-defined environmental factors.

<img src="assets/Demand Matrix.png" alt="Predictive 7-Day Demand Curve" width="100%" />

---

### 4. Machine Learning Sensitivity & Attribution Matrix
Comparative horizontal feature importance distribution showing the exact mathematical weight computed by the Random Forest core nodes across individual telemetry vector inputs.

<img src="assets/Feature Importance.png" alt="Feature Attribution Matrices" width="100%" />

---

## Directory Structure

```text
smart_energy_optimization/
│
├── data/                             # Dataset storage repository
│   ├── daily_dataset.csv             # Raw London smart meter volumetric data (~99MB)
│   └── weather_hourly_darksky.csv    # Historical hourly weather telemetry records
│
├── models/
│   └── energy_forecast_model.pkl     # Serialized Random Forest core regression artifact
│
├── notebooks/
│   └── Main.ipynb                    # Exploratory Data Analysis & training workbook
│
├── src/
│   ├── __init__.py                   # Python package structural declaration
│   ├── data_pipeline.py              # Data loading, cleaning, and inner join synchronization
│   ├── feature_eng.py                # Temporal feature engineering suite
│   └── model_pipeline.py             # Model initialization, ensemble training, and serialization
│
├── app/
│   └── gui_app.py                    # Streamlit interactive user UI dashboard script
│
└── requirements.txt                  # Project runtime environment dependencies manifest
