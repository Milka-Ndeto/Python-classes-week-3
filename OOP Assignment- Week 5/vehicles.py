# Parent Class: Vehicle
class Vehicle:
    def move(self):
        return "The vehicle moves."

# Child Class: Car
class Car(Vehicle):
    def move(self):
        return "The car drives on the road. 🚗"

# Child Class: Plane
class Plane(Vehicle):
    def move(self):
        return "The plane flies in the sky. ✈️"

# Child Class: Boat
class Boat(Vehicle):
    def move(self):
        return "The boat sails on water. 🚤"

# Creating objects
car = Car()
plane = Plane()
boat = Boat()

# Using polymorphism
vehicles = [car, plane, boat]

for v in vehicles:
    print(v.move())
