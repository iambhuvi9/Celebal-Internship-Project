import pandas as pd

def extract_temporal_features(df):
    # Extract granular temporal vectors from raw date stamps
    df['day'] = pd.to_datetime(df['day'])
    df['Month'] = df['day'].dt.month
    df['Day_of_Week'] = df['day'].dt.weekday
    df['Is_Weekend'] = df['Day_of_Week'].apply(lambda x: 1 if x >= 5 else 0)
    return df