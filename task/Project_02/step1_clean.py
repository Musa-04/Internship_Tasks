import pandas as pd
import numpy as np

df = pd.read_csv("data/telco_churn.csv")

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)
df.drop('customerID', axis=1, inplace=True)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

df.to_csv("data/telco_churn_clean.csv", index=False)
print("Cleaned dataset saved!")
print(f"Shape: {df.shape}")
print(df['Churn'].value_counts())