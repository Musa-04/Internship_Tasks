class Dog:
    def sound(self): print("Bark")

class Cat:
    def sound(self): print("Meow")

for a in [Dog(), Cat()]:
    a.sound()
