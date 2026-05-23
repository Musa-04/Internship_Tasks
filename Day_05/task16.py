class Employee:
    def calculate_salary(self):
        return 30000

class Manager(Employee):
    def calculate_salary(self):
        return 60000

print(Manager().calculate_salary())
