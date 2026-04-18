import pandas as pd
import os

df = pd.read_csv("data/ecommerce_raw.csv")

print("=== BEFORE CLEANING ===")
print(f"Shape: {df.shape}")
print(f"\nMissing values:\n{df.isnull().sum()}")
print(f"\nDuplicates: {df.duplicated().sum()}")
print(f"\nData types:\n{df.dtypes}")

# Fix date column
df['Date'] = pd.to_datetime(df['Date'])

# Extract useful time features
df['Month']    = df['Date'].dt.month
df['DayOfWeek']= df['Date'].dt.dayofweek
df['Hour']     = df['Date'].dt.hour
df['Year']     = df['Date'].dt.year

# Drop duplicates if any
df.drop_duplicates(inplace=True)

# Save
df.to_csv("data/ecommerce_clean.csv", index=False)

print("\n=== AFTER CLEANING ===")
print(f"Shape: {df.shape}")
print(f"\nSample:\n{df.head()}")
print("\n✅ Cleaned dataset saved!")