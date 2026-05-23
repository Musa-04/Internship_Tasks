# Task 02: Internship Eligibility Checker
# Scenario: Check eligibility based on CGPA and year

cgpa = float(input("Enter CGPA: "))
year = int(input("Enter year of study: "))

if cgpa >= 7.0 and year >= 3:
    print("Eligible for internship")
else:
    print("Not eligible for internship")
