⚡ Autonomous Energy Optimization Platform for Smart Grids

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualization-blueviolet)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

An intelligent machine learning platform for **energy consumption forecasting** using smart meter telemetry and historical weather data.

The project combines **Random Forest Regression**, weather analytics, temporal feature engineering, and an interactive **Streamlit dashboard** to forecast electricity demand, visualize future consumption trends, and generate rule-based energy optimization recommendations.

---

# Project Overview

Electricity demand is influenced by several environmental and temporal factors such as temperature, humidity, wind speed, weekdays, weekends, and seasonal changes.

This platform:

- Loads smart meter energy consumption data
- Integrates historical weather information
- Performs feature engineering
- Trains a Random Forest Regression model
- Predicts future electricity demand
- Displays results using an interactive Streamlit dashboard
- Generates optimization recommendations based on predicted demand

---

# Features

- Smart Meter Data Processing Pipeline
- Weather Data Integration
- Temporal Feature Engineering
- Random Forest Regression Model
- 7-Day Energy Demand Forecast
- Feature Importance Visualization
- Interactive Streamlit Dashboard
- Plotly Interactive Charts
- Rule-Based Energy Optimization Suggestions
- Serialized Machine Learning Model using Joblib

---

# Project Preview

## 1. Enterprise SaaS Dashboard Core Layout

The unified analytics frame maps predictive capabilities against real-time operational constraints across an optimized multi-column enterprise SaaS configuration:

- **Primary Left Navigation Sidebar**: Hosts interactive control modules, split into the `🌡️ Telemetry Simulation Matrix` and `📅 Temporal Modifiers` control clusters.
- **Main Mainframe Column (Center-Left Grid)**: Processes the primary `🔮 AI Core Forecasted Load Profile` indicator block directly above the continuous `📈 Predictive 7-Day Demand Matrix` trend tracker.
- **Operational Intelligence Column (Right Grid)**: Aggregates real-time diagnostic telemetry outputs under the `🧠 Autonomous Optimization Engine` log array alongside the `📊 Quantified Grid Optimization Level` health index bar.
- **Lower Analytics Control Block (Full-Width Base Floor)**: Spans horizontally across the complete dashboard workspace layout, embedding the comprehensive `📊 Feature Attribution Matrices (Sensitivity Index)` to isolate variable coefficients instantly.

<img src="assets/Dashboard Platform.png" width="100%">

---

## 2. Input Simulation Panel (Dynamic Parameter Boundary Configuration)

The control center sidebar exposes two granular input vector sub-modules to dynamically simulate and stress-test the machine learning model's predictive limits:

- **🌡️ Telemetry Simulation Matrix**: Real-time physical parameter sliders to configure ambient conditions, including Minimum Temperature (°C), Maximum Temperature (°C), Relative Humidity, and Wind Velocity (mph).
- **📅 Temporal Modifiers Engine**: Houses a master activation toggle (`Enable Temporal Analytics Engine`) that opens interactive target constraints: a calendar date picker (`Select Target Date`), a diurnal shift matrix selector (`Day Shift` / `Night Shift`), and a Target Operating Hour granular scheduler.

<img src="assets/Telemetry Input.png" width="100%">

---

## 3. Predictive 7-Day Demand Matrix (Volumetric Load Tracking)

An interactive load tracker that receives synchronized feature inputs to project cyclic grid consumption trajectories over a forward-looking weekly horizon:

- **Dynamic X-Axis Projection**: Adapts automatically to map localized sequential sequences starting from the targeted base tracking profile (`Day 1 (Mon)` through `Day 7 (Sun)`).
- **Y-Axis Scalability**: Tracks absolute metrics directly in Kilowatt-hours (`kWh`) across continuous grid intervals to isolate cyclic load variances at a glance.
- **AI Core Synchronization**: Linked dynamically to the primary forecast card, reflecting minor adjustments instantly as you change values on the telemetry sliders.

<img src="assets/Demand Matrix.png" width="100%">

---

## 4.1 Autonomous Optimization Engine & Grid Health Metrics

A highly reactive diagnostic interface panel that maps multi-variable environmental telemetry inputs directly to automated grid efficiency rules and operational action logs. The engine evaluates physics limits and calendar constraints dynamically to dispatch real-time system badges:

### 🧠 Real-Time Dynamic Grid Action Logs & Scenarios

The optimization engine continuously parses system states to trigger specific tracking loops:

#### A. Thermal Sensitivity Management (`Min/Max Temperature` Triggers)
* **`⛅ AMBIENT BALANCE` (Standard Mode)**: Active when microclimate fields remain within comfortable baselines ($18^\circ\text{C}$ to $24^\circ\text{C}$). Localized HVAC infrastructure operations fall back to standard runtime settings.
* **`❄️ THERMAL DROP ACTIVE` (Heating Demand Override)**: Automatically dispatches severe low-temperature alerts when maximum temperatures drop below $15^\circ\text{C}$. The engine overrides standard parameters to throttle building auxiliary loads and optimize core thermal comfort.
* **`🔥 THERMAL PEAK CRISIS` (Cooling Mitigation Mode)**: Engages instantly when ambient limits breach $30^\circ\text{C}$. Drops auxiliary targets and triggers active demand-side management overrides to prevent localized grid transformation failures.

#### B. Moisture & Latent Load Processing (`Relative Humidity` Triggers)
* **`💧 STABLE MOISTURE PROFILE` (Normal Humidity)**: Confirms relative moisture vectors are operating within the optimal tracking index ($0.45$ to $0.65$). Eliminates extra condensation or cooling cycle load weights.
* **`⚠️ LATENT LOAD CRISIS` (Dehumidification Override)**: Triggered by heavy saturation parameters ($\text{Humidity} > 0.75$). The core algorithm initiates dedicated moisture extraction routines to balance grid pressures caused by latent climate load conditions.

#### C. Convective Air Movement Operations (`Wind Velocity` Triggers)
* **`🍃 KINETIC DRAFT LOCK` (High HVAC Load Protection)**: Triggered when wind draft velocities surge past $25\text{ mph}$. Closes automated ventilation dampers to reduce building infiltration loads and convective heat loss vectors.
* **`🌬️ CONVECTIVE BENEFIT ACTIVE` (Free-Cooling Mode)**: Active during moderate external wind profiles ($8\text{ mph}$ to $15\text{ mph}$) combined with warm internal limits. The engine utilizes natural ventilation cycles to cool the grid infrastructure without spinning up heavy compressor units.

#### D. Operational Routine Alignment (`Temporal Modifiers` Triggers)
* **`💼 ENTERPRISE ALIGNMENT MATRIX` (Commercial Peak Load)**: Engages automatically when the `Temporal Analytics Engine` is active on standard working weekdays (`Monday` to `Friday`) during high-activity business windows (`08:00` to `18:00`). Initiates strict consumption containment and peak-pricing mitigation sequences.
* **`🏡 RESIDENTIAL SHIFT CURVE` (Weekend Drop Mode)**: Triggered immediately when the tracking calendar maps weekend indices (`Is_Weekend = 1`). Shifts efficiency priorities from commercial clusters to domestic supply optimization models.
* **`🔒 TEMPORAL LOGIC OFFLINE` (Standalone Physics Mode)**: Displays when the master temporal analytics switch is explicitly disabled. The engine bypasses calendar structures entirely, running analytics models based purely on physical climate vectors.

---

### 4.2 Quantified Grid Optimization Level

The system constantly runs cross-validation equations against input variables to generate a dynamic grid optimization target index:

- **Unified Status Monitor**: Displays an active system health value using a dark progress visualization track.
- **Efficiency Metrics**: Evaluates the real-time conservation baseline. When conditions match perfectly (e.g., matching the `AMBIENT BALANCE` state), it outputs a high running index score of **`80/100`** or higher.
- **Automatic Adjustments**: The index drops responsively when complex weather states happen at the same time (e.g., experiencing low temperatures alongside a `LATENT LOAD CRISIS`), providing clear mathematical warnings to operators.

<img src="assets/Optimization Logs.png" width="100%">
---

## 5. Machine Learning Sensitivity & Attribution Matrix (Attribution Weights)

A diagnostic plot displaying the exact global feature attribution scores across the core ensemble algorithm. It ranks factors by their sensitivity coefficients to give clear mathematical transparency to users:

- **Attribution Distribution**: Shows how environmental vectors (`Max Temp`, `Min Temp`, `Humidity`, `Wind Speed`) compare directly against structural calendar elements (`Month`, `Day of Week`, `Is Weekend`).
- **Dynamic Structural Floor**: Spans horizontally across the complete interface floor, demonstrating that the `Max Temp` threshold stands as the primary mathematical contributor driving the core regression logic.
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

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Cleaning & Processing |
| NumPy | Numerical Computing |
| Scikit-Learn | Machine Learning |
| Random Forest Regressor | Energy Forecasting |
| Plotly | Interactive Charts |
| Streamlit | Dashboard Development |
| Joblib | Model Serialization |

---

# Machine Learning Pipeline

```text
          Smart Meter Dataset
                    │
                    ▼
         Weather Dataset
                    │
                    ▼
          Data Cleaning & Merge
                    │
                    ▼
        Feature Engineering
   (Month • Weekday • Weekend)
                    │
                    ▼
      Random Forest Regression
                    │
                    ▼
      Energy Consumption Prediction
                    │
                    ▼
       Optimization Recommendations
                    │
                    ▼
         Streamlit Dashboard
```

---

# Dataset

## Smart Meter Dataset

Contains daily electricity consumption collected from London Smart Meters.

Main target variable:

- **energy_sum**

---

## Weather Dataset

Historical weather variables including:

- Temperature Max
- Temperature Min
- Humidity
- Wind Speed

These variables are merged with the energy dataset for prediction.

---

# Feature Engineering

The following features are extracted:

- Month
- Day of Week
- Weekend Flag
- Maximum Temperature
- Minimum Temperature
- Humidity
- Wind Speed

---

# Model

The forecasting engine uses:

**Random Forest Regressor**

### Input Features

- temperatureMax
- temperatureMin
- humidity
- windSpeed
- month
- day_of_week
- weekend

### Target

```
energy_sum
```

---

# Dashboard Features

The Streamlit application provides:

- Temperature Controls
- Humidity Slider
- Wind Speed Input
- Calendar Selection
- 7-Day Energy Forecast
- Feature Importance Chart
- Energy Optimization Alerts
- Interactive Plotly Visualizations

---

# Optimization Rules

The platform generates simple rule-based recommendations such as:

- High Cooling Demand Expected
- Reduce HVAC Load During Peak Hours
- High Wind Efficiency
- Weekend Low Demand
- Balanced Grid Condition

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/smart-energy-optimization.git

cd smart-energy-optimization
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Train the Model

Open the notebook

```
notebooks/Main.ipynb
```

Run all cells.

This will:

- Load datasets
- Process data
- Train the Random Forest model
- Save

```
models/energy_forecast_model.pkl
```

---

# Run the Dashboard

```bash
streamlit run app/gui_app.py
```

Open

```
http://localhost:8501
```

---

# Example Workflow

```
Weather Data
        │
        ▼
Feature Engineering
        │
        ▼
Random Forest Prediction
        │
        ▼
7-Day Energy Forecast
        │
        ▼
Optimization Suggestions
        │
        ▼
Interactive Dashboard
```

---

# Future Improvements

- XGBoost Model
- LightGBM Integration
- LSTM Time-Series Forecasting
- Real-Time Smart Meter API
- Cloud Deployment
- Docker Support
- CI/CD Pipeline
- Grid-Level Demand Analytics

---

# Dataset Source

- London Smart Meter Dataset
- DarkSky Historical Weather Dataset

---

# Author

**Bhavesh Gorana**

B.Tech Computer Science (Data Science)

JIET, Jodhpur

---

# License

This project is developed for educational and research purposes.
