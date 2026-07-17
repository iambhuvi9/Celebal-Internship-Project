import pandas as pd

def extract_temporal_features(df):
    """
    Extracts granular temporal vectors from raw date stamps.
    """
    df['day'] = pd.to_datetime(df['day'])
    df['Month'] = df['day'].dt.month
    df['Day_of_Week'] = df['day'].dt.weekday
    df['Is_Weekend'] = df['Day_of_Week'].apply(lambda x: 1 if x >= 5 else 0)
    return df

def build_lag_features(df):
    """
    Calculates historical target lags and rolling baselines chronologically per household.
    """
    df = df.sort_values(by=['LCLid', 'day']).reset_index(drop=True)
    
    # Yesterday's consumption
    df['energy_lag_1'] = df.groupby('LCLid')['energy_sum'].shift(1)
    
    # Same day last week
    df['energy_lag_7'] = df.groupby('LCLid')['energy_sum'].shift(7)
    
    # 3-day window average shifted past current row
    df['energy_rolling_mean_3'] = (
        df.groupby('LCLid')['energy_sum']
        .shift(1)
        .rolling(window=3, min_periods=1)
        .mean()
    )
    
    # Drop rows without complete historical profiles
    subset_cols = ['energy_lag_1', 'energy_lag_7', 'energy_rolling_mean_3']
    return df.dropna(subset=subset_cols).copy()