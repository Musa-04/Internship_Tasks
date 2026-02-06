# Task 01: Employee Salary Calculator
# Scenario: Calculate monthly salary after bonus and tax

basic_salary = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus amount: "))
tax = float(input("Enter tax amount: "))

final_salary = basic_salary + bonus - tax

print("Final Monthly Salary:", final_salary)
