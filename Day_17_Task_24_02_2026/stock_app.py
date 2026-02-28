import tkinter as tk
from tkinter import messagebox
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock():
    symbol = entry.get()

    if symbol == "":
        messagebox.showerror("Error", "Enter Stock Symbol")
        return

    data = yf.download(symbol, period="6mo")

    if data.empty:
        messagebox.showerror("Error", "Invalid Stock Symbol")
        return

    data["MA50"] = data["Close"].rolling(20).mean()

    plt.figure()
    plt.plot(data["Close"], label="Close Price")
    plt.plot(data["MA50"], label="Moving Avg")
    plt.legend()
    plt.title(symbol + " Stock Price")
    plt.show()

root = tk.Tk()
root.title("Stock Price Prediction")

tk.Label(root, text="Enter Stock Symbol (AAPL, TSLA)").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Predict", command=fetch_stock).pack(pady=10)

root.mainloop()