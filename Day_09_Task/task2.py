
import numpy as np

marks = np.array([85, 92, 78, 90, 88])

# Sort marks
sorted_marks = np.sort(marks)[::-1]
print("Sorted marks (high to low):", sorted_marks)

# Ranking using argsort
rank = np.argsort(marks)[::-1]
print("Ranking index:", rank)

print("Top student mark:", marks[rank[0]])
