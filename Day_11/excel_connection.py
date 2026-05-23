import pandas as pd

# Create sample DataFrame
data = {
    "Name": ["Aman", "Riya", "Rahul"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# Save to Excel
df.to_excel("students.xlsx", index=False)

# Read from Excel
new_df = pd.read_excel("students.xlsx")

print(new_df)