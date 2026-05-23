# Task 01: Student Grade Calculator

def calculate_grade(marks):
    percentage = sum(marks) / len(marks)

    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

print(calculate_grade([80, 70, 75, 90]))


# Task 02: ATM Withdrawal

def withdraw(balance, amount):
    if amount <= balance and amount % 100 == 0:
        return balance - amount
    else:
        return "Invalid withdrawal"

print(withdraw(10000, 2000))


# Task 03: Password Validator

def password_validator(password):
    if (len(password) >= 8 and
        any(c.isdigit() for c in password) and
        any(c.isupper() for c in password)):
        return "Valid Password"
    else:
        return "Invalid Password"

print(password_validator("Python123"))
