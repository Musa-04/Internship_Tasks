class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print(self.name, self.rollno, self.marks)

s1 = Student("Ayaan", 1, 85)
s2 = Student("Aiza", 2, 90)
s3 = Student("Ali", 3, 78)

s1.display()
s2.display()
s3.display()
