# Basic user-defined functions

def greet():
    print("Hello welcome to the session")

greet()


def addition(a, b):
    return a + b

print(addition(5, 9))


def subtraction(x, y):
    return x - y

print(subtraction(10, 4))


def square(num):
    return num * num

print(square(4))


def info(name):
    print("Hello", name)

info("Tabassum")
info("Pujitha")


def greet_user(name="Guest"):
    print("Hello", name)

greet_user("Ayaan")
greet_user()
