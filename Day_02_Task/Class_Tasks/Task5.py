# Task 05: Course Enrollment Validator
# Scenario: Check if student enrolled in Python course

courses = ["Python", "Data Science", "AI"]

course_name = input("Enter course name to check: ")

if course_name in courses:
    print("Student is enrolled in", course_name)
else:
    print("Student is not enrolled in", course_name)
