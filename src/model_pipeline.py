import os
import numpy as np
import joblib
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Unified 10-feature matrix mapping matching feature_eng outputs
FEATURE_COLS = [
    'temperatureMax', 'temperatureMin', 'humidity', 'windSpeed', 
    'Month', 'Day_of_Week', 'Is_Weekend',
    'energy_lag_1', 'energy_lag_7', 'energy_rolling_mean_3'
]
TARGET_COL = 'energy_sum'

def train_and_save_model(X, y, save_path):
    """
    Initializes high-capacity LightGBM Regressor, tracks error reduction 
    metrics via an verification split, and exports the serialized model artifact.
    """
    # 80/20 train/test evaluation split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # High-Capacity LightGBM architecture config
    model = lgb.LGBMRegressor(
        n_estimators=1000,       
        learning_rate=0.05,     
        num_leaves=63,          
        subsample=0.8,          
        colsample_bytree=0.8,   
        force_row_wise=True,    
        random_state=42,
        n_jobs=-1               
    )
    
    print("Training LightGBM core regression platform with lag telemetry...")
    model.fit(
        X_train, 
        y_train,
        eval_set=[(X_test, y_test)],
        callbacks=[lgb.early_stopping(stopping_rounds=30, verbose=True)]
    )
    
    # Perform performance validation
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    print("\n==============================")
    print("      EVALUATION RESULTS      ")
    print("==============================")
    print(f"R² Score: {r2:.4f}")
    print(f"RMSE    : {rmse:.4f}")
    print("==============================")
    
    # Ensure directory existence and serialize artifact
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    joblib.dump(model, save_path)
    print(f"Model successfully exported to {save_path}")
    
    return model