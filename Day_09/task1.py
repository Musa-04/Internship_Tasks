import numpy as np

# rows = regions, columns = months
sales = np.array([
    [2000, 2500, 3000, 2800],   # Region 1
    [1500, 1800, 2200, 2100],   # Region 2
    [3000, 3200, 3500, 3700]    # Region 3
])

# 1. Total sales per region
total_region = np.sum(sales, axis=1)
print("Total sales per region:", total_region)

# 2. Average sales per month
avg_month = np.mean(sales, axis=0)
print("Average sales per month:", avg_month)

# 3. Best performing region
best_region = np.argmax(total_region)
print("Best performing region:", best_region+1)
