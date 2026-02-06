def add_student(name):
    with open("students.txt", "a") as f:
        f.write(name + "\n")

def view_students():
    with open("students.txt", "r") as f:
        print(f.read())

def search_student(name):
    with open("students.txt", "r") as f:
        for line in f:
            if name.lower() in line.lower():
                print("Student Found:", line)
                return
    print("Student not found")

add_student("Ayaan")
view_students()
search_student("Ayaan")
