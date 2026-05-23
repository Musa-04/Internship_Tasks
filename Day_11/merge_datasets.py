import pandas as pd

# Customer Data
customers = {
    "customer_id": ["C1","C2","C3"],
    "customer_name": ["Aman","Riya","Rahul"],
    "city": ["Hyderabad","Delhi","Mumbai"]
}

customer_df = pd.DataFrame(customers)

# Order Data
orders = {
    "order_id": [101,102,103],
    "customer_id": ["C1","C2","C3"],
    "amount": [5000,7000,3000]
}

order_df = pd.DataFrame(orders)

# Merge
merged_df = pd.merge(customer_df, order_df, on="customer_id")

print("Merged Data:")
print(merged_df)