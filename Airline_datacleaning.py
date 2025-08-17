import pandas as pd

# Loading CSV file from kaggle
df = pd.read_csv("airline_passenger_sample.csv")

# Strip spaces from column names
df.columns = [col.strip().replace(" ", "").replace("/", "").replace("-", "") for col in df.columns]

# Fixing typos in categorical columns
df['Gender'] = df['Gender'].replace({'Fermale':'Female'})
df['TypeOfTravel'] = df['TypeOfTravel'].replace({'PersonalTravel':'Personal'})

# Filling missing numeric values with median
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Filling missing categorical values with mode
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Dropping duplicates
df.drop_duplicates(inplace=True)

# Save the cleaned CSV
df.to_csv("airline_passenger_cleaned.csv", index=False)

print("Data cleaning completed. Cleaned CSV saved as 'airline_passenger_cleaned.csv'.")
