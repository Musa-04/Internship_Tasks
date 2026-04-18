import pandas as pd

url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
df = pd.read_csv(url)

df.to_csv("data/telco_churn.csv", index=False)
print("Dataset saved!")
print(f"Shape: {df.shape}")
print(df.head())