class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2 * (self.l + self.w)

r = Rectangle(5, 4)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
