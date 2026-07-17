# Installation & Deployment

1. Clone Repository & Navigate
bash
git clone https://github.com/yourusername/smart-energy-optimization.git
cd smart-energy-optimization

```

## 2. Initialize Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate

```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate

```

## 3. Install Requirements

```bash
pip install -r requirements.txt

```

## 4. Compile the Pipeline & Train AI Core Engine

Execute the main pipeline training script from the project root. This process runs the complete ingestion chain, computes multi-dimensional features, executes the LightGBM regressor optimization loop, and dumps the serialized model:

```bash
python run_pipeline.py

```

## 5. Boot Up the Asynchronous Control Dashboard

Launch the interactive enterprise dashboard interface:

```bash
streamlit run app/gui_app.py

```

---

# Dataset References
