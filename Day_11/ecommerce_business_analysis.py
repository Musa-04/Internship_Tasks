import pandas as pd

# E-commerce Dataset
ecommerce = {
    "order_id": [1001,1002,1003,1004,1005],
    "date": ["2025-01-02","2025-01-03","2025-02-10","2025-02-15","2025-03-03"],
    "customer_id": ["C101","C102","C103","C104","C105"],
    "region": ["NORTH","SOUTH","EAST","WEST","NORTH"],
    "product_name": ["Headphones","T-shirts","AC","Shoes","Laptops"],
    "quantity": [1,2,2,3,1],
    "price": [1500,700,125000,1000,100000]
}

df = pd.DataFrame(ecommerce)

df["date"] = pd.to_datetime(df["date"])
df["total"] = df["quantity"] * df["price"]

print("Full Dataset:")
print(df)

# Total Revenue
print("\nTotal Revenue:")
print(df["total"].sum())

# Top Products
print("\nTop Products:")
print(df.groupby("product_name")["total"].sum().sort_values(ascending=False))

# Monthly Trend
df["month"] = df["date"].dt.month
print("\nMonthly Sales Trend:")
print(df.groupby("month")["total"].sum())

# High Value Customers (>100000)
customer_sales = df.groupby("customer_id")["total"].sum()
print("\nHigh Value Customers:")
print(customer_sales[customer_sales > 100000])

# Regional Performance
print("\nRegional Performance:")
print(df.groupby("region")["total"].sum())