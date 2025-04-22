# Base class representing a generic Vehicle
class Vehicle:
    def move(self):
        pass  # This will be overridden in child classes


# Car class - Inherits from Vehicle and defines move() differently
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


# Plane class - Inherits from Vehicle and defines move() differently
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


# Base class representing an Animal
class Animal:
    def move(self):
        pass  # This will be overridden in child classes


# Dog class - Inherits from Animal and defines move() differently
class Dog(Animal):
    def move(self):
        print("Running 🐕")


# Bird class - Inherits from Animal and defines move() differently
class Bird(Animal):
    def move(self):
        print("Flying 🦅")


# Create instances of the classes
vehicle1 = Car()
vehicle2 = Plane()
animal1 = Dog()
animal2 = Bird()

# Demonstrate polymorphism by calling the move() method on different objects
vehicle1.move()  # Outputs: Driving 🚗
vehicle2.move()  # Outputs: Flying ✈️
animal1.move()   # Outputs: Running 🐕
animal2.move()   # Outputs: Flying 🦅
