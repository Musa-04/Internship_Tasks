class Laptop:
    def __init__(self, serial):
        self.__serial = serial

    def get_serial(self):
        return "Access Restricted"

l = Laptop("ABC123")
print(l.get_serial())
