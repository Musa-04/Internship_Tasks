class Staff:
    def work(self):
        print("Staff working")

class Teacher(Staff):
    def teach(self):
        print("Teaching")

Teacher().work()
