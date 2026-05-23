# File Handling Basics

# Write to file
f = open("demo_file.txt", "w")
f.write("The different modes are read, write, append etc")
f.close()

# Read file
f = open("demo_file.txt", "r")
print(f.read())
f.close()

# Append to file
f = open("demo_file.txt", "a")
f.write("\nFile handling is easy in Python")
f.close()

# Read using with statement
with open("demo_file.txt", "r") as f:
    print(f.read())
