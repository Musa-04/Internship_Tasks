class Product:
    def __init__(self, price):
        self._price = price

class Child(Product):
    def show(self):
        print(self._price)

c = Child(500)
c.show()
