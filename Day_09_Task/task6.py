import numpy as np

# employee id, age, salary
emp = np.array([
    [1, 25, 30000],
    [2, 30, 40000],
    [3, 35, 50000],
    [4, 28, 42000],
    [5, 30, 40000]
])

# names list
names = np.array(["Arjun", "Ravi", "Sita", "Ravi", "Kiran"])

# correlation between age & salary
age = emp[:,1]
salary = emp[:,2]

corr = np.corrcoef(age, salary)
print("Correlation between age & salary:\n", corr)

# mean salary
print("Mean salary:", np.mean(salary))

# duplicate names
unique, counts = np.unique(names, return_counts=True)
duplicates = unique[counts > 1]
print("Duplicate names:", duplicates)
