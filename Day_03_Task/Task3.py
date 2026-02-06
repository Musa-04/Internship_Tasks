# TASK 03: PASSWORD VALIDATOR
# Requirements:
# - minimum 8 characters
# - at least 1 digit
# - at least 1 uppercase


def password_validator(password):
    if (len(password) >= 8 and
        any(char.isdigit() for char in password) and
        any(char.isupper() for char in password)):
        return "Valid Password"
    else:
        return "Invalid Password"

print(password_validator("Python123"))
print(password_validator("python"))