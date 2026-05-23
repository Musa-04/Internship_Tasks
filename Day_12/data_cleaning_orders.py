import pandas as pd
import numpy as np

print("\n=========== ORIGINAL DATA ===========\n")

# Create messy dataset
data = {
    "order_id": [1001, 1002, 1003, 1003, 1004],
    "customer_id": ["C101", "C102", "C103", "C103", "C104"],
    "gender": ["M", "F", "male", "male", "f"],
    "age": [25, None, 150, 150, -5],
    "city": ["Hyderabad", None, "Mumbai", "Mumbai", None],
    "product_category": ["Electronics", "fashion", "ELECTRONICS", "ELECTRONICS", "Fashion"],
    "price": [50000, 2000, 30000, 30000, 1500],
    "product_name": ["Laptop", "T-shirt", "Mobile", "Mobile", "Shoes"],
    "quantity": [1, 2, 1, 1, 3],
    "order_date": ["2025-01-01", "2025-02-10", "2025-03-15", "2025-03-15", "2025-04-20"]
}

df = pd.DataFrame(data)
print(df)


# ============================================================
# 1️⃣ REMOVE DUPLICATE ORDERS (based on order_id)
# ============================================================

df = df.drop_duplicates(subset=["order_id"])

# ============================================================
# 2️⃣ FIX GENDER COLUMN
# ============================================================

df["gender"] = df["gender"].str.lower()
df["gender"] = df["gender"].replace({
    "m": "male",
    "f": "female"
})



# Replace invalid ages with NaN
df.loc[(df["age"] > 100) | (df["age"] < 0), "age"] = np.nan

# Fill missing ages with mean
df["age"] = df["age"].fillna(df["age"].mean())


df["city"] = df["city"].fillna(df["city"].mode()[0])


df["product_category"] = df["product_category"].str.lower().str.strip()


df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")


df.columns = df.columns.str.lower()

print("\n=========== CLEANED DATA ===========\n")
print(df)

print("\n=========== DATA TYPES ===========\n")
print(df.dtypes)