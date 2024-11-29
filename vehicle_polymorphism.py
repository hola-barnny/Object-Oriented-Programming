# Base class: Vehicle
class Vehicle:
    def move(self):
        print("The vehicle is moving")

# Derived class: Car (polymorphism in action)
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Derived class: Plane (polymorphism in action)
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Derived class: Boat (polymorphism in action)
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Polymorphism example
def start_journey(vehicle: Vehicle):
    vehicle.move()

# Create instances of each class
car = Car()
plane = Plane()
boat = Boat()

# Call the move method on different objects
start_journey(car)    # Output: Driving 🚗
start_journey(plane)  # Output: Flying ✈️
start_journey(boat)   # Output: Sailing 🚢
