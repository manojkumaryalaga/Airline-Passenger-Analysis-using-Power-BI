import pandas as pd
import numpy as np

# Load CSV file
df = pd.read_csv("airline_passenger_sample.csv")

# Clean column names
df.columns = [col.strip().replace(" ", "").replace("/", "").replace("-", "") for col in df.columns]

# Fill missing numeric values using NumPy median
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    df[col].fillna(np.median(df[col].values), inplace=True)

# Fill missing categorical values with mode
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Save cleaned CSV
df.to_csv("airline_passenger_cleaned.csv", index=False)

print("Data cleaning completed. Cleaned CSV saved as 'airline_passenger_cleaned.csv'.")
