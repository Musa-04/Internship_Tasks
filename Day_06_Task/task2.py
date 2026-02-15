class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   # list of marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

    def display(self):
        print("Name:", self.name)
        print("Total:", self.calculate_total())
        print("Average:", self.calculate_average())
        print("Grade:", self.grade())


# Test
s1 = Student("Rahul", [85, 90, 88, 92, 87])
s1.display()
