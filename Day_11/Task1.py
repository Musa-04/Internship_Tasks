import pandas as pd

# Create Employee DataFrame
employees = {
    "name": ["Aman", "Riya", "Rahul", "Sneha", "Arjun"],
    "dept": ["IT", "HR", "IT", "Finance", "HR"],
    "salary": [60000, 45000, 75000, 50000, 48000]
}

df = pd.DataFrame(employees)

print("Full Data:")
print(df)

# Filter by Department
print("\nEmployees in IT:")
print(df[df["dept"] == "IT"])

# Group By Department
print("\nAverage Salary by Department:")
print(df.groupby("dept")["salary"].mean())