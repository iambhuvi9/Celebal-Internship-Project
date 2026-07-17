# Autonomous Energy Optimization Platform for Smart Grids

---

An intelligent machine learning platform for **real-time energy consumption forecasting** and automated demand-side mitigation using smart meter telemetry, socio-economic context profiles, and historical weather data arrays.

The project leverages an optimized **LightGBM Regressor engine**, dynamic temporal feature tracking, rolling historical lag resolution matrices, and a high-tech premium **Streamlit enterprise dashboard framework** to forecast localized electricity load patterns, track complex grid sensitivities, and dispatch immediate rule-based grid directives.

---

# Project Overview

Electricity infrastructure demand is highly volatile, driven by non-linear interactions between immediate physical microclimates, continuous time-series history, cultural holiday patterns, and varying socio-economic household footprints.

This platform:
- Ingests localized smart meter energy consumption streams alongside historical darksky weather metrics.
- Integrates macroeconomic context tables including historical UK Bank Holiday distributions and structural household ACORN classifications.
- Resolves sequential continuous properties via engineering multi-day rolling averages and deep historical lags.
- Maximizes regression efficiency by training a production-grade LightGBM Ensemble core.
- Streamlines grid operations via a high-performance interactive Streamlit dashboard mapping dynamic physics parameter adjustments to automated operational rule directives.

---

# Features

- **Multi-Dimensional Ingestion Pipeline**: Joint synchronization across smart meter logs, granular weather vectors, bank holidays, and household categories.
- **LightGBM Gradient Boosting Engine**: Advanced regression framework tuned with early-stopping criteria to prevent over-fitting while maximizing predictive efficiency.
- **12-Feature Dynamic Matrix**: Processes composite inputs mapping environmental parameters alongside complex lag profiles and categorical variables simultaneously.
- **Rolling Time-Series Resolution**: Automatically computes 1-day/7-day historical offsets alongside 3-day continuous rolling load means per household identifier (`LCLid`).
- **Autonomous Optimization Logging**: Rule-based automation dispatch engine that translates sensor parameters into color-coded microgrid alerts and mitigation actions.
- **SaaS Premium Grid Visualizations**: High-contrast interface styling mapping weekly forecasting trajectories and global feature sensitivity indexes via native Streamlit interactive visual components.

---

# Project Preview

## 1. Enterprise SaaS Dashboard Core Layout
The unified analytics frame maps predictive capabilities against real-time operational constraints across an optimized multi-column enterprise SaaS configuration:
- **Primary Left Navigation Sidebar**: Hosts interactive control modules, split into the `🏠 Focus Context` filter, `🌡️ Telemetry Simulation Matrix`, and `📅 Temporal Modifiers` control clusters.
- **Main Mainframe Column (Center-Left Grid)**: Processes the primary `🔮 AI Core Forecasted Load Profile` indicator block directly above the continuous `📈 Predictive 7-Day Demand Matrix` trend tracker.
- **Operational Intelligence Column (Right Grid)**: Aggregates real-time diagnostic telemetry outputs under the `🧠 Autonomous Optimization Engine` log array alongside the `📊 Quantified Grid Optimization Level` health index bar.
- **Lower Analytics Control Block (Full-Width Base Floor)**: Spans horizontally across the complete dashboard workspace layout, embedding the comprehensive `📊 Feature Attribution Matrices (Sensitivity Index)` to isolate variable coefficients instantly.
<img src="assets/Dashboard Platform.png" width="100%">

## 2. Input Simulation Panel (Dynamic Parameter Boundary Configuration)
The control center sidebar exposes three granular input vector sub-modules to dynamically simulate and stress-test the machine learning model's predictive limits:
- **🏠 Focus Context**: Dropdown selection allowing real-time targeting of unique household profiles (`LCLid`), automatically extracting corresponding historical baseline configurations and categorical groupings.
- **🌡️ Telemetry Simulation Matrix**: Real-time physical parameter sliders to configure ambient conditions, including Minimum Temperature (°C), Maximum Temperature (°C), Relative Humidity, and Wind Velocity (mph).
- **📅 Temporal Modifiers Engine**: Houses a master activation toggle (`Enable Temporal Analytics Engine`) that opens interactive target constraints: a calendar date picker (`Select Target Date`), a diurnal shift matrix selector (`Day Shift` / `Night Shift`), and a Target Operating Hour granular scheduler.
<img src="assets/Input Slider.png" width="50%">

## 3. Predictive 7-Day Demand Matrix (Volumetric Load Tracking)
An interactive load tracker that receives synchronized feature inputs to project cyclic grid consumption trajectories over a forward-looking weekly horizon:
- **Dynamic X-Axis Projection**: Adapts automatically to map localized sequential sequences starting from the targeted base tracking profile (`Day 1` through `Day 7`).
- **Y-Axis Scalability**: Tracks absolute metrics directly in Kilowatt-hours (`kWh`) across continuous grid intervals to isolate cyclic load variances at a glance.
- **AI Core Synchronization**: Linked dynamically to the primary forecast card, reflecting minor adjustments instantly as you change values on the telemetry sliders.
<img src="assets/Demand Matrix.png" width="100%">

## 4.1 Autonomous Optimization Engine & Grid Health Metrics
A highly reactive diagnostic interface panel that maps multi-variable environmental telemetry inputs directly to automated grid efficiency rules and operational action logs. The engine evaluates physics limits and calendar constraints dynamically to dispatch real-time system badges:

### 🧠 Real-Time Dynamic Grid Action Logs & Scenarios

#### A. Thermal Sensitivity Management (`Min/Max Temperature` Triggers)
* **`🌤️ AMBIENT BALANCE` (Standard Mode)**: Active when microclimate fields remain within comfortable baselines ($15^\circ\text{C}$ to $30^\circ\text{C}$). Localized HVAC infrastructure operations fall back to standard runtime settings.
* **`❄️ THERMAL DROP ACTIVE` (Heating Demand Override)**: Automatically dispatches low-temperature alerts when maximum temperatures drop below $15^\circ\text{C}$. The engine overrides standard parameters to trigger building auxiliary loads and limit core thermal bleeding.
* **`⚠️ THERMAL PEAK ACTIVE` (Cooling Mitigation Mode)**: Engages instantly when ambient limits breach $30^\circ\text{C}$. Drops auxiliary targets and triggers active demand-side management overrides to throttle HVAC system compressors to a strict efficiency ceiling.

#### B. Moisture & Latent Load Processing (`Relative Humidity` Triggers)
* **`💧 STABLE MOISTURE PROFILE` (Normal Humidity)**: Confirms relative moisture vectors are operating within the optimal tracking index ($\text{Humidity} \le 0.75$). Eliminates extra condensation or cooling cycle load weights.
* **`💧 LATENT LOAD CRISIS` (Dehumidification Override)**: Triggered by heavy saturation parameters ($\text{Humidity} > 0.75$). The core algorithm initiates dedicated moisture extraction routines, reconfiguring the framework to dry mode balancing.

#### C. Convective Air Movement Operations (`Wind Velocity` Triggers)
* **`🍃 KINETIC DRAFT LOCK` (High HVAC Load Protection)**: Triggered when wind velocity surges past $15\text{ mph}$ under low-temperature parameters ($\text{Temperature Max} < 15^\circ\text{C}$), keeping mechanical draft channels securely locked.
* **`🍃 KINETIC DRAFT BENEFIT` (Free-Cooling Mode)**: Active during high ambient wind velocity profiles ($\text{Wind Speed} > 15\text{ mph}$) combined with warm, moderate conditions ($18^\circ\text{C} \le \text{Temperature Max} \le 28^\circ\text{C}$). The engine cuts supply to mechanical cooling substations and opens passive air shafts.

#### D. Operational & Cultural Routine Alignment (`Temporal Modifiers` Triggers)
* **`🎉 UK BANK HOLIDAY ACTIVE` (Macroeconomic Baseline Shift)**: Dynamically overrides routine calendar assumptions if the selected date maps against the processed UK Bank Holiday schedule, shifting base parameters to off-peak conservation baselines.
* **`🌙 NIGHT CYCLE OPTIMIZATION` (Diurnal Energy Mode)**: Minimizes auxiliary facility lighting and engages structural thermal preservation targets during night-shift constraints.
* **`💼 ENTERPRISE ALIGNMENT MATRIX` / `🏠 RESIDENTIAL SHIFT CURVE`**: Segregates operational parameters automatically depending on weekday/weekend tracking indices (`Is_Weekend`), triggering strict peak-load monitoring or residential morning block optimization logs accordingly.

---

### 4.2 Quantified Grid Optimization Level
The system constantly runs cross-validation equations against input variables to generate a dynamic grid optimization target index:
- **Unified Status Monitor**: Displays an active system health value using a dark progress visualization track.
- **Efficiency Metrics**: Evaluates the real-time conservation baseline relative to expected peak thresholds, presenting an explicit efficiency coefficient index score (e.g., `59/100`).

<img src="assets/Optimization Logs.png" width="100%">

---

## 5. Machine Learning Sensitivity & Attribution Matrix (Attribution Weights)
A diagnostic plot displaying the exact global feature attribution scores across the core ensemble algorithm. It ranks factors by their sensitivity coefficients to give clear mathematical transparency to users:
- **Attribution Distribution**: Shows how environmental vectors (`Max Temp`, `Min Temp`, `Humidity`, `Wind Speed`) compare directly against structural calendar elements (`Month`, `Day of Week`, `Is Weekend`), calendar holiday states (`is_bank_holiday`), demographic constraints (`acorn_encoded`), and historical trends.
- **Dynamic Structural Floor**: Spans horizontally across the complete interface floor, demonstrating that the `Max Temp` threshold and `Lag 1 Day` values stand as the primary mathematical contributors driving the core regression logic.
- **Visual Mapping**: Features high-contrast pink column vectors aligned perfectly within dark canvas grids to make tracking sensitivities simple for operators at a glance.
<img src="assets/Feature Importance.png" width="100%">
---

# Directory Structure

```text
smart_energy_optimization/
│
├── app/
│   └── gui_app.py
│
├── assets/
│   ├── Dashboard Platform.png
│   ├── Telemetry Input.png
│   ├── Demand Matrix.png
│   └── Feature Importance.png
│
├── data/
│   ├── daily_dataset.csv
│   └── weather_hourly_darksky.csv
│
├── models/
│   └── energy_forecast_model.pkl
│
├── notebooks/
│   └── Main.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_pipeline.py
│   ├── feature_eng.py
│   └── model_pipeline.py
│
├── requirements.txt
│
└── README.md
```

# ⚡ Autonomous Energy Optimization Platform

AI‑Driven Predictive Grid Analytics & Automated Demand‑Side Optimization Engine

---

# 🚀 Technology Stack

| Technology      | Purpose                                                                 |
|-----------------|-------------------------------------------------------------------------|
| **Python**      | Central execution language framework                                    |
| **Pandas**      | Hierarchical dataset cleaning, relational joins & merging               |
| **NumPy**       | Multi‑dimensional array configurations & vectorized functions           |
| **LightGBM**    | High‑performance gradient boosting regression engine                    |
| **Scikit‑Learn**| Validation splitting matrices & model performance scoring metrics       |
| **Streamlit**   | Core asynchronous UI layout & reactive widget component architecture    |
| **Joblib**      | Fast pipeline serialization & model object storage                      |

---

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




* **London Smart Meter Telemetry Dataset**: Localized residential power consumption timelines.
* **DarkSky Historical Weather Dataset**: Contextual atmospheric telemetry parameters matching the exact geographic boundary windows.
