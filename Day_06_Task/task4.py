# Base class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.__salary = base_salary   # private variable

    def get_salary(self):
        return self.__salary

    def calculate_salary(self):
        return self.__salary


# Manager class
class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.get_salary() + self.bonus


# Intern class
class Intern(Employee):
    def __init__(self, name, base_salary, stipend):
        super().__init__(name, base_salary)
        self.stipend = stipend

    def calculate_salary(self):
        return self.get_salary() + self.stipend


# Store employees
employees = []

m1 = Manager("Arjun", 50000, 10000)
i1 = Intern("Ravi", 10000, 2000)

employees.append(m1)
employees.append(i1)

# Payroll display
print("---- PAYROLL ----")
for emp in employees:
    print(emp.name, "Salary:", emp.calculate_salary())
