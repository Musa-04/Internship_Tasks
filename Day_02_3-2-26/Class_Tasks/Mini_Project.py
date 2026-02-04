# Mini Project: Performance Rating System
# Scenario: Assign performance rating based on performance score

score = int(input("Enter performance score: "))

if score >= 90:
    rating = "Excellent"
elif score >= 75:
    rating = "Good"
elif score >= 60:
    rating = "Average"
else:
    rating = "Poor"

print("Performance Rating:", rating)
