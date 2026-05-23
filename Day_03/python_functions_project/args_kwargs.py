# *args and **kwargs examples

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(10, 20, 30, 40))


def show_marks_students(name, *scores):
    print("Name:", name)
    print("Scores:", scores)

show_marks_students("Alishba", 80, 89, 95)


def employee_details(**kwargs):
    print(kwargs)

employee_details(Name="Alishba", Age=27, City="Hyderabad")


def register_user(**user):
    print("USER REGISTRATION DETAILS:")
    for key, value in user.items():
        print(key, "=", value)

register_user(username="Shaheda123", Email="shah@gmail.com")
