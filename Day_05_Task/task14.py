class Shape: pass

class Circle(Shape):
    def area(self, r):
        return 3.14 * r * r

class Rectangle(Shape):
    def area(self, l, w):
        return l * w

print(Circle().area(5))
