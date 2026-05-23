# MINI PROJECT: Employee Salary Calculator

def employee_salary(basic):
    hra = 0.20 * basic
    pf = 0.12 * basic
    net_salary = basic + hra - pf
    return net_salary

basic_salary = float(input("Enter basic salary: "))
print("Net Salary:", employee_salary(basic_salary))
