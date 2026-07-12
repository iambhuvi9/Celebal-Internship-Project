import os
import pandas as pd

def load_and_clean_data(data_dir):
    # Utilizing low_memory=False optimization due to large dataset footprint
    df_energy = pd.read_csv(os.path.join(data_dir, 'daily_dataset.csv'), low_memory=False)
    df_weather = pd.read_csv(os.path.join(data_dir, 'weather_hourly_darksky.csv'))
    
    # Data type conversion logic goes here (converting dates to datetime, strings to float)
    
    return df_energy, df_weather

def merge_datasets(df_energy, df_weather):
    # Synchronize both datasets via an inner join constraint on the 'day' vector
    df_merged = pd.merge(df_energy, df_weather, on='day', how='inner')
    return df_merged.dropna()