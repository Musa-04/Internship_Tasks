class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show(self):
        print(self.title, "-", self.author)

b = Book("Python", "Guido")
b.show()
