import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt

df = None

# =========================
# Upload CSV File
# =========================
def upload_csv():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if file_path:
        try:
            df = pd.read_csv(file_path)
            messagebox.showinfo("Success", "CSV Loaded Successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file\n{e}")

# =========================
# Clean Data
# =========================
def clean_data():
    global df
    
    if df is None:
        messagebox.showwarning("Warning", "Please upload CSV first!")
        return

    df.drop_duplicates(subset=["order_id"], inplace=True)

    df["gender"] = df["gender"].str.lower()
    df["gender"] = df["gender"].replace({"m": "male", "f": "female"})

    df.loc[(df["age"] > 100) | (df["age"] < 0), "age"] = np.nan
    df["age"] = df["age"].fillna(df["age"].mean())

    df["city"] = df["city"].fillna(df["city"].mode()[0])

    df["product_category"] = df["product_category"].str.lower().str.strip()

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    messagebox.showinfo("Success", "Data Cleaned Successfully!")

# =========================
# Business Analysis
# =========================
def analyze_data():
    global df
    
    if df is None:
        messagebox.showwarning("Warning", "Please upload CSV first!")
        return

    df["total_revenue"] = df["price"] * df["quantity"]

    total_revenue = df["total_revenue"].sum()
    city_sales = df.groupby("city")["total_revenue"].sum().sort_values(ascending=False)
    category_sales = df.groupby("product_category")["total_revenue"].sum().sort_values(ascending=False)

    result_box.delete("1.0", tk.END)

    result_box.insert(tk.END, f"TOTAL REVENUE: {total_revenue}\n\n")
    result_box.insert(tk.END, "TOP CITIES BY SALES:\n")
    result_box.insert(tk.END, city_sales.to_string())
    result_box.insert(tk.END, "\n\nCATEGORY-WISE SALES:\n")
    result_box.insert(tk.END, category_sales.to_string())

# =========================
# SHOW CHARTS
# =========================
def show_charts():
    global df
    
    if df is None:
        messagebox.showwarning("Warning", "Please upload CSV first!")
        return

    df["total_revenue"] = df["price"] * df["quantity"]

    city_sales = df.groupby("city")["total_revenue"].sum()
    category_sales = df.groupby("product_category")["total_revenue"].sum()

    # Bar Chart - City Sales
    plt.figure()
    city_sales.plot(kind="bar")
    plt.title("Top Cities by Sales")
    plt.xlabel("City")
    plt.ylabel("Total Revenue")
    plt.show()

    # Pie Chart - Category Sales
    plt.figure()
    category_sales.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Category-wise Sales")
    plt.ylabel("")
    plt.show()

# =========================
# GUI Design
# =========================
root = tk.Tk()
root.title("E-Commerce Data Analyst Dashboard")
root.geometry("800x650")
root.configure(bg="#f4f6f9")

title = tk.Label(root,
                 text="E-Commerce Data Analyst Dashboard",
                 font=("Arial", 18, "bold"),
                 bg="#f4f6f9",
                 fg="#1a237e")
title.pack(pady=15)

button_frame = tk.Frame(root, bg="#f4f6f9")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Upload CSV",
          bg="#4caf50", fg="white",
          width=18, command=upload_csv).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Clean Data",
          bg="#2196f3", fg="white",
          width=18, command=clean_data).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="Run Analysis",
          bg="#ff9800", fg="white",
          width=18, command=analyze_data).grid(row=0, column=2, padx=10)

tk.Button(button_frame, text="Show Charts",
          bg="#9c27b0", fg="white",
          width=18, command=show_charts).grid(row=0, column=3, padx=10)

result_box = tk.Text(root, height=20, width=95)
result_box.pack(pady=20)

root.mainloop()