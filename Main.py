import pandas as pd
import subprocess
from pathlib import Path
from Importing_Data import upload_info

# Start uploading data
fips, NIBRS_dataset = upload_info()

# Save each dataset as a CSV file
fips.to_csv("fips.csv", index = False)
for id, df in NIBRS_dataset.items():
    df.to_csv(f"NIBRS_{id}_2023.csv", index = False)

print(fips.shape)

# Clean the datasets process from Jupyter Notebook
subprocess.run([
    "jupyter", "nbconvert",
    "--to", "notebook",
    "--execute", "--inplace",
    "Cleaning Data.ipynb"
])

# Pull in the datasets to utilize for analysis
Crime_Data_State = pd.read_csv('Crime_Data_State.csv')
Officer_Data_State = pd.read_csv('Officer_Data_State.csv')
Overall_Data = pd.read_csv('Overall_Data.csv')
Summarized_Data = pd.read_csv('Summarized_Data.csv')

# Ensure they pulled in properly
print(f"Crime_Data_State shape: {Crime_Data_State.shape}")
print(f"Officer_Data_State shape: {Officer_Data_State.shape}")
print(f"Overall_Data shape: {Overall_Data.shape}")
print(f"Summarized_Data shape: {Summarized_Data.shape}")
