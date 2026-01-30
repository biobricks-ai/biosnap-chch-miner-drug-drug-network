import pandas as pd
import os

try:
    df = pd.read_parquet("brick/data.parquet")
    print("Successfully read parquet file.")
    print(df.head())
    print(df.shape)
    print(df.columns)
except Exception as e:
    print(f"Failed to read parquet: {e}")
