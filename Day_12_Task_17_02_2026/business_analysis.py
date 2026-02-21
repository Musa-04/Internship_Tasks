import pandas as pd
import numpy as np

print("\n=========== CREATING CLEAN DATASET ===========\n")

# Sample cleaned dataset (after Part 1 cleaning)
data = {
    "order_id": [1001, 1002, 1003, 1004],
    "customer_id": ["C101", "C102", "C103", "C104"],
    "gender": ["male", "female", "male", "female"],
    "age": [25, 30, 35, 28],
    "city": ["Hyderabad", "Mumbai", "Mumbai", "Hyderabad"],
    "product_category": ["electronics", "fashion", "electronics", "fashion"],
    "price": [50000, 2000, 30000, 1500],
    "product_name": ["Laptop", "T-shirt", "Mobile", "Shoes"],
    "quantity": [1, 2, 1, 3],
    "order_date": pd.to_datetime(["2025-01-01", "2025-02-10", "2025-03-15", "2025-04-20"])
}

df = pd.DataFrame(data)

print(df)


df["total_revenue"] = df["price"] * df["quantity"]

total_revenue = df["total_revenue"].sum()

print("\n=========== TOTAL REVENUE ===========")
print("Total Revenue:", total_revenue)




city_sales = df.groupby("city")["total_revenue"].sum().sort_values(ascending=False)

print("\n=========== TOP CITIES BY SALES ===========")
print(city_sales)



category_sales = df.groupby("product_category")["total_revenue"].sum().sort_values(ascending=False)

print("\n=========== CATEGORY-WISE SALES ===========")
print(category_sales)