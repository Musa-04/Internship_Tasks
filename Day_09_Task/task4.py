import numpy as np

prices = np.array([100, 200, 300, 400])
tax = 0.18   # 18% GST

# broadcasting
final_price = prices + (prices * tax)
print("Final prices after tax:", final_price)
