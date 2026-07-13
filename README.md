# ⚡ Autonomous Energy Optimization Platform for Smart Grids

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

The unified analytics frame maps predictive capabilities against real-time operational constraints across a multi-column layout structure:

- **Primary Left Navigation Sidebar**: Controls global simulation parameters across telemetry arrays and temporal model variables.
- **Center Analytics Dashboard**: Tracks immediate dynamic scalar load indicators alongside a continuous 7-Day consumption spline grid.
- **Right Automation Engine Log**: Outputs prioritized tactical optimization override badges and responsive localized system health index states.
- **Lower Analytics Control Panel**: Benchmarks feature contribution variance metrics asynchronously derived from the underlying ensemble nodes.

<img src="assets/Dashboard Platform.png" width="100%">
---

## 2. Input Simulation Panel (Dynamic Parameter Boundary Configuration)

The control center sidebar exposes two granular input vector sub-modules to dynamically stress-test the model's predictive limits:

- **🌡️ Telemetry Simulation Matrix**: Configures immediate raw physics parameters using precision sliders including Minimum/Maximum Temperature thresholds (°C), Relative Humidity levels, and Wind Velocity metrics (mph).
- **📅 Temporal Modifiers Engine**: Integrates a master toggle button to dynamically switch between standalone weather parsing or complete date-driven logic. Exposes an active calendar selector, diurnal phase tracking (`Day Shift` vs. `Night Shift`), and hourly granular sliders (`00:00` to `23:00`).

<img src="assets/Telemetry Input.png" width="100%">
---

## 3. Predictive 7-Day Demand Matrix (Volumetric Load Tracking)

An interactive temporal load tracker that receives synchronized feature inputs to project cyclic grid consumption trajectories over a forward-looking weekly horizon:

- **Dynamic X-Axis Projection**: Adapts automatically to map labels starting from the selected calendar date sequence (e.g., `Day 1 (Mon)` through `Day 7 (Sun)`).
- **Y-Axis Scalability**: Tracks absolute metrics directly in Kilowatt-hours (`kWh`) to catch localized peak load spikes.
- **Plotly Integration Upgrade**: (Optional) In the codebase, this step updates the standard native layout into an absolute `plotly.graph_objects.Scatter` model with a `shape='spline'` parameter to render smooth area trends over raw stepped structures.

<img src="assets/Demand Matrix.png" width="100%">
---
## 4. Machine Learning Sensitivity & Attribution Matrix (Attribution Weights)

A diagnostic plot displaying the exact global feature attribution scores across the core ensemble algorithm. It ranks factors by their sensitivity coefficients to give clear mathematical transparency to users:

- **Attribution Distribution**: Shows how environmental vectors (`MaxTemp`, `MinTemp`, `Humidity`, `Wind Speed`) compare directly against calendar elements (`Month`, `Day of Week`, `Is Weekend`).
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
