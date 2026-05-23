# TASK 04: EMPLOYEE SALARY CALCULATOR
# Requirements:
# - HRA = 20%
# - PF = 12%
# - return net salary

def employee_salary(basic):
    hra = 0.20 * basic
    pf = 0.12 * basic
    net_salary = basic + hra - pf
    return net_salary

print(employee_salary(30000))