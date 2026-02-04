#internship task
cgpa = float(input("Enter CGPA: "))
year = int(input("Enter year of study: "))
skill_score = int(input("Enter skill test score: "))

if cgpa >= 7.0 and year >= 3 and skill_score >= 60:
    print("Eligible for internship")
else:
    print("Not eligible")
