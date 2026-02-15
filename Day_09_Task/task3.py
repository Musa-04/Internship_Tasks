import numpy as np

quality = np.array([95, 88, 92, 70, 85, 98])

# Pass if >80
passed = quality[quality > 80]
failed = quality[quality <= 80]

print("Passed products:", passed)
print("Failed products:", failed)

print("Pass percentage:", len(passed)/len(quality)*100)
