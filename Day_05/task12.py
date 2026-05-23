class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, eid):
        super().__init__(name, age)
        self.eid = eid

e = Employee("Ali", 25, 101)
print(e.name, e.age, e.eid)
