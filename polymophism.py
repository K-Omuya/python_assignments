# Base class
class Vehicle:
    def move(self):
        pass  # Placeholder method (can be abstract in advanced cases)

# Subclasses with their own move() behavior
class Car(Vehicle):
    def move(self):
        return "Driving "

class Plane(Vehicle):
    def move(self):
        return "Flying "

class Boat(Vehicle):
    def move(self):
        return "Sailing "

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling "

# Testing polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    print(v.move())
