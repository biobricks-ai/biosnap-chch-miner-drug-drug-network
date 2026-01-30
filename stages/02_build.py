import pandas as pd
import gzip
import os

input_path = "download/ChCh-Miner_durgbank-chem-chem.tsv.gz"
output_path = "brick/data.parquet"

# Check if file exists
if not os.path.exists(input_path):
    raise FileNotFoundError(f"{input_path} not found")

# Read the file
# SNAP files usually have comments at the top
with gzip.open(input_path, 'rt') as f:
    # Read first few lines to check for header
    # Usually SNAP files don't have a header, but have comments
    df = pd.read_csv(f, sep='\t', comment='#', header=None, names=['drug_a', 'drug_b'])

# Drop duplicates if any
df = df.drop_duplicates()

# Save to parquet
df.to_parquet(output_path, index=False)

print(f"Converted {input_path} to {output_path}. Shape: {df.shape}")
