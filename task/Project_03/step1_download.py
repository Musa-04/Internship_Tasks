import pandas as pd
import numpy as np
import os

np.random.seed(42)
os.makedirs("data", exist_ok=True)

n = 10000  # 10,000 transactions

products = [
    'Laptop', 'Phone', 'Headphones', 'Keyboard', 'Mouse',
    'Monitor', 'Tablet', 'Charger', 'Speaker', 'Webcam',
    'T-Shirt', 'Jeans', 'Shoes', 'Jacket', 'Watch',
    'Book', 'Pen', 'Notebook', 'Backpack', 'Sunglasses'
]

categories = {
    'Laptop':'Electronics', 'Phone':'Electronics', 'Headphones':'Electronics',
    'Keyboard':'Electronics', 'Mouse':'Electronics', 'Monitor':'Electronics',
    'Tablet':'Electronics', 'Charger':'Electronics', 'Speaker':'Electronics',
    'Webcam':'Electronics', 'T-Shirt':'Clothing', 'Jeans':'Clothing',
    'Shoes':'Clothing', 'Jacket':'Clothing', 'Watch':'Accessories',
    'Book':'Stationery', 'Pen':'Stationery', 'Notebook':'Stationery',
    'Backpack':'Accessories', 'Sunglasses':'Accessories'
}

prices = {
    'Laptop':80000, 'Phone':50000, 'Headphones':3000, 'Keyboard':2000,
    'Mouse':1000, 'Monitor':20000, 'Tablet':30000, 'Charger':800,
    'Speaker':4000, 'Webcam':2500, 'T-Shirt':500, 'Jeans':1500,
    'Shoes':3000, 'Jacket':4000, 'Watch':5000, 'Book':300,
    'Pen':50, 'Notebook':200, 'Backpack':2000, 'Sunglasses':1500
}

product_col  = np.random.choice(products, n)
customer_ids = np.random.randint(1000, 2000, n)
quantities   = np.random.randint(1, 6, n)
ratings      = np.random.choice([1, 2, 3, 4, 5], n, p=[0.05, 0.1, 0.2, 0.35, 0.3])
price_col    = [prices[p] * np.random.uniform(0.9, 1.1) for p in product_col]
dates        = pd.date_range("2022-01-01", periods=n, freq='1h')

df = pd.DataFrame({
    'CustomerID':  customer_ids,
    'Product':     product_col,
    'Category':    [categories[p] for p in product_col],
    'Quantity':    quantities,
    'Price':       np.round(price_col, 2),
    'Rating':      ratings,
    'TotalAmount': np.round(np.array(price_col) * quantities, 2),
    'Date':        dates,
    'City':        np.random.choice(['Mumbai','Delhi','Bangalore','Chennai','Hyderabad'], n),
    'PaymentMethod': np.random.choice(['UPI','Card','NetBanking','COD'], n,
                                       p=[0.4, 0.3, 0.2, 0.1])
})

df.to_csv("data/ecommerce_raw.csv", index=False)
print("Dataset created!")
print(f"Shape: {df.shape}")
print(df.head())
print("\nColumns:", df.columns.tolist())