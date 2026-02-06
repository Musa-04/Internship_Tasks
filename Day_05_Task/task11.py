class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle): pass
class Bus(Vehicle): pass
class Bike(Vehicle): pass

Car().start()
Bike().start()
