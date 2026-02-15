# Base class
class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

# Child class
class Book(LibraryItem):
    def __init__(self, title, author, book_id):
        super().__init__(title, author)
        self.book_id = book_id
        self.__available = True   # encapsulated variable

    def issue_book(self):
        if self.__available:
            self.__available = False
            print(f"{self.title} issued successfully")
        else:
            print("Book not available")

    def return_book(self):
        self.__available = True
        print(f"{self.title} returned")

    def status(self):
        print("Available" if self.__available else "Not Available")


# Test
b1 = Book("Python Basics", "Guido", 101)
b1.display_info()
b1.status()
b1.issue_book()
b1.status()
