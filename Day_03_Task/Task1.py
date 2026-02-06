# TASK 01: STUDENT GRADE CALCULATOR

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

print(calculate_grade([80, 75, 70, 85]))