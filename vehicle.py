# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Car class
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Boat class
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Function to demonstrate polymorphism
def demonstrate_movement(vehicle):
    vehicle.move()

# Example usage
car = Car()
plane = Plane()
boat = Boat()

demonstrate_movement(car)   # Output: Driving 🚗
demonstrate_movement(plane)  # Output: Flying ✈️
demonstrate_movement(boat)   # Output: Sailing ⛵
