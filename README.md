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
---

###  Tech Stack & System Workflow Matrix
Is part me dependencies lookup definitions aur analytical sequential components workflow block mapping hai:

```markdown
---

## Tech Stack

| Technology | Purpose |
|:---|:---|
| **Scikit-Learn** | Core machine learning framework utilized for ensemble training and model validation loops. |
| **Streamlit** | Fast Python UI library utilized to build the reactive, high-tech single-page analytics application. |
| **Plotly Express/GO** | Deploys responsive, highly interactive, premium spline charts and horizontal bar graphs. |
| **Pandas & NumPy** | Handles heavy mathematical transformations, low-memory array configurations, and data vector merges. |
| **Joblib** | Specialized serialization utility for freezing and exporting the trained ML artifact weights. |

---

## Analytics & Predictive Architecture

The automated demand-side management and consumption forecasting workflow operates through a structured vector extraction pipeline:

```text
[Smart Meter Array Data]                [Weather Telemetry Streams]
           │                                         │
           ▼                                         ▼
┌────────────────────────────────────────────────────────────┐
│                  Data Processing Engine                    │
│      (Low-Memory Filtering + Datetime Type Enforcement)    │
└──────────────────────────────┬─────────────────────────────┘
                               │
                               ▼
┌────────────────────────────────────────────────────────────┐
│                Inner Join Constraint Node                  │
│             (Synchronized via shared 'day' vector)          │
└──────────────────────────────┬─────────────────────────────┘
                               │
                               ▼
┌────────────────────────────────────────────────────────────┐
│                 Feature Engineering Suite                  │
│        (Extracts Month, Day of Week, and Weekend Flags)     │
└──────────────────────────────┬─────────────────────────────┘
                               │
                               ▼
┌────────────────────────────────────────────────────────────┐
│             Random Forest Regressor Core Node              │
│         (Maps Multi-Variable Meteorological Vectors)       │
└──────────────────────────────┬─────────────────────────────┘
                               │
                               ▼
 ┌─────────────────────────────┴─────────────────────────────┐
 │               Autonomous Optimization Engine              │
 └─────────────────────────────┬─────────────────────────────┘
                               │
          ┌────────────────────┴────────────────────┐
          ▼                                         ▼
[⚠️ THERMAL / MOISTURE ALERTS]             [🟢 GRID BALANCED STATE]
(Dispatches HVAC Throttle Directives)      (Stabilizes System Baseline)

---

###  Installation Guide & Verification Logs
Is part me terminal configurations shell commands, running strategies aur dynamic kaggle metadata pointers hain:

```markdown
---

## Quick Start & Installation (Step-by-Step)

Follow these directions to initialize, compile, and spin up the architecture within your local environment setup:

### 1. Open Terminal and Navigate to Project Folder
Open your PowerShell or Command Prompt window and move into the absolute system repository pathway:
```powershell
cd D:\Smart_Energy_Optimization

### 2. Initialize the Isolated Virtual Environment
Create a sandboxed Python execution frame to clean block native system dependencies conflicts:

```powershell
python -m venv venv

### 3. Activate the Environment Sandbox
Engage the environment structure depending on your host terminal shell mapping:
# On Windows PowerShell:
venv\Scripts\Activate.ps1

# On Windows Command Prompt:
venv\Scripts\activate.bat

### 4. Install Component Dependencies
Pull down and link all required numerical processing, learning frameworks, and charting packages:
python -m pip install -r requirements.txt

### 5. Execute Core Machine Learning Pipeline
Open the notebooks/Main.ipynb file or run the underlying scripts in sequence. This ingests the raw source datasets, runs the data engineering modules, trains the Random Forest model, and dumps the artifact (energy_forecast_model.pkl) straight into the models/ directory.

### 6. Launch the Local SaaS Dashboard
Execute the production server script block to boot the web interface engine instantly:
streamlit run app/gui_app.py
The application dashboard will automatically bind to your network stack and spin up in your default web browser tracking interface at http://localhost:8501.

### Running the Application
Telemetry Simulation Setup: Adjust the temperature sliders, humidity levels, and wind speeds on the sidebar panel to emulate varying structural grid pressures.

Temporal Controls Evaluation: Toggle the Master Temporal Switch. When active, select specific dates, day shifts (Day/Night), and peak-pricing hours. Turning it OFF bypasses calendar arrays to focus purely on climate values.

Automated Log Extraction: Review the right column (Autonomous Optimization Engine) to analyze real-time dynamic badges (e.g., Thermal Drop Active, Latent Load Crisis, or Temporal Logic Offline) dispatched by the optimization logic.

### References & Data Citations
Target Energy Dataset: Ingests the public Smart Meters in London Dataset hosted on Kaggle, analyzing continuous volumetric smart meter tracking entries spanning 5,500 London households.

Historical Weather Streams: Linked directly against DarkSky hourly weather profiles containing localized multi-spectral variables (including relative humidity indexes, wind velocities, and minimum/maximum daily temperatures).
