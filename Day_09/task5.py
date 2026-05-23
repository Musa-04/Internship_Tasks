import numpy as np

# customer id, age, purchase amount, region
data = np.array([
    [1, 25, 5000, 1],
    [2, 30, 7000, 2],
    [3, 22, 3000, 1],
    [4, 35, 9000, 3],
    [5, 28, 6000, 2]
])

# 1 total customers
print("Total customers:", data.shape[0])

# 2 extract purchase column
purchase = data[:,2]
print("Purchase column:", purchase)

# 3 average purchase
avg_purchase = np.mean(purchase)
print("Average purchase:", avg_purchase)

# 4 max & min purchase
print("Max purchase:", np.max(purchase))
print("Min purchase:", np.min(purchase))

# 5 customers above average
above_avg = data[purchase > avg_purchase]
print("Customers above average purchase:\n", above_avg)
