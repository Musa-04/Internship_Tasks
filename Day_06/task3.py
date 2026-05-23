class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price   # encapsulation

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price

    def display(self):
        print(f"Product: {self.name}, Price: ₹{self.__price}")


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def total_amount(self):
        total = 0
        for p in self.items:
            total += p.get_price()
        return total

    def show_cart(self):
        print("Cart Items:")
        for p in self.items:
            p.display()
        print("Total:", self.total_amount())


# Test
p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 500)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
cart.show_cart()
