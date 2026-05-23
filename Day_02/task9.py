students = [
    {"name": "A", "cgpa": 7.5},
    {"name": "B", "cgpa": 6.2},
    {"name": "C", "cgpa": 8.1}
]

for s in students:
    if s["cgpa"] >= 7:
        print(s["name"], "shortlisted")
