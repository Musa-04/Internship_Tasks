import pandas as pd

# Create Product DataFrame
sales_data = {
    "product_id": ["P1","P2","P3","P4","P5","P6"],
    "product_name": ["Laptop","Mobile","TV","Shoes","Watch","Tablet"],
    "quantity": [5,10,3,20,7,4],
    "price": [100000,30000,50000,2000,10000,40000]
}

df = pd.DataFrame(sales_data)

# Calculate Total Sales
df["total_sales"] = df["quantity"] * df["price"]

print("Sales Data:")
print(df)

# Top 5 Products
print("\nTop 5 Products Based on Sales:")
print(df.sort_values(by="total_sales", ascending=False).head(5))