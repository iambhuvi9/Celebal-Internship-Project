import os
import pandas as pd

def load_and_clean_data(data_dir):
    """
    Ingests energy and hourly weather datasets, applies explicit data type 
    conversions, and aggregates weather observations to a daily grain.
    """
    # Utilizing low_memory=False optimization due to large dataset footprint
    df_energy = pd.read_csv(os.path.join(data_dir, 'daily_dataset.csv'), low_memory=False)
    df_weather = pd.read_csv(os.path.join(data_dir, 'weather_hourly_darksky.csv'))
    
    # --- Energy Processing & Type Conversions ---
    df_energy['day'] = pd.to_datetime(df_energy['day'])
    if 'energy_sum' in df_energy.columns:
        df_energy['energy_sum'] = pd.to_numeric(df_energy['energy_sum'], errors='coerce')
    elif 'energy_median' in df_energy.columns:
        df_energy['energy_sum'] = pd.to_numeric(df_energy['energy_median'], errors='coerce')
        
    # --- Weather Processing & Type Conversions ---
    df_weather['time'] = pd.to_datetime(df_weather['time'])
    df_weather['day'] = df_weather['time'].dt.floor('D')
    
    # Automatically map fields based on name matches
    temp_col = next((c for c in df_weather.columns if "temp" in c.lower()), None)
    humidity_col = next((c for c in df_weather.columns if "humid" in c.lower()), None)
    wind_col = next((c for c in df_weather.columns if "wind" in c.lower()), None)
    
    agg_dict = {}
    rename_dict = {}
    
    if temp_col:
        agg_dict[temp_col] = ['max', 'min']
        rename_dict[f"{temp_col}_max"] = "temperatureMax"
        rename_dict[f"{temp_col}_min"] = "temperatureMin"
    if humidity_col:
        agg_dict[humidity_col] = ['mean']
        rename_dict[f"{humidity_col}_mean"] = "humidity"
    if wind_col:
        agg_dict[wind_col] = ['mean']
        rename_dict[f"{wind_col}_mean"] = "windSpeed"
        
    # Aggregate hourly columns to daily records
    daily_weather = df_weather.groupby('day').agg(agg_dict)
    daily_weather.columns = ['_'.join(col).strip('_') for col in daily_weather.columns]
    daily_weather = daily_weather.reset_index().rename(columns=rename_dict)
    
    return df_energy, daily_weather

def merge_datasets(df_energy, df_weather):
    """
    Synchronizes both datasets via an inner join constraint on the 'day' vector
    and drops missing values introduced during aggregation.
    """
    df_merged = pd.merge(df_energy, df_weather, on='day', how='inner')
    return df_merged.dropna()