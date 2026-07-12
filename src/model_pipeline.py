import joblib
from sklearn.ensemble import RandomForestRegressor

def train_and_save_model(X, y, save_path):
    # Initialize and train advanced ensemble regression architecture
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Save the AI core regression artifact for downstream GUI application usage
    joblib.dump(model, save_path)
    print(f"Model successfully exported to {save_path}")