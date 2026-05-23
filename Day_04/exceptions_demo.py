# Division error
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Name error
try:
    print(Name)
except NameError:
    print("Variable not defined")

# Index error
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range")

# Key error
try:
    student = {"name": "Rahul"}
    print(student["age"])
except KeyError:
    print("Key not found")

# Value error
try:
    x = int("abc")
except ValueError:
    print("Invalid integer value")
