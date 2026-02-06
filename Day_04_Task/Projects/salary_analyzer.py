import csv

try:
    salaries = []

    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            salaries.append(int(row["salary"]))

    print("Highest Salary:", max(salaries))
    print("Lowest Salary:", min(salaries))
    print("Average Salary:", sum(salaries) / len(salaries))

except FileNotFoundError:
    print("Employees file not found")
except ValueError:
    print("Invalid salary data")
