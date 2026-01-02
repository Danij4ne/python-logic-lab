
"""
Ex03 - Vehicle Class Hierarchy

Description:
    Create a base class Vehicle and two subclasses: Car and Motorcycle.
    Each subclass should have its own specific behavior or attribute.

Requirements:
    - Define a base class named Vehicle.
    - The Vehicle class should have:
        - a brand attribute
        - a model attribute
        - a method display_info() that prints brand and model
    - Create a subclass Car that:
        - inherits from Vehicle
        - has an additional attribute, for example: doors
        - overrides display_info() to include the number of doors
    - Create a subclass Motorcycle that:
        - inherits from Vehicle
        - has an additional attribute, for example: has_sidecar (True/False)
        - overrides display_info() to include sidecar information
    - In the main part of the script, create a Car and a Motorcycle
      and call display_info() on both.

Notes:
    - The focus is on inheritance and method overriding.
    - Attributes can be hard-coded; no user input is required.

Example (expected behavior):
    Car: Toyota Corolla, Doors: 4
    Motorcycle: Harley Davidson, Sidecar: False
"""

# TODO:
# 1. Define the Vehicle base class with brand, model, and display_info().
# 2. Create Car and Motorcycle subclasses with additional attributes.
# 3. Override display_info() in both subclasses.
# 4. Create examples and call display_info() on each.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(self.brand, self.model)


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Doors: {self.doors}")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar=False):
        super().__init__(brand, model)
        self.has_sidecar = has_sidecar

    def display_info(self):
        print(f"Motorcycle: {self.brand} {self.model}, Sidecar: {self.has_sidecar}")


 
car = Car("Toyota", "Corolla", 4)
motorcycle = Motorcycle("Harley", "Davidson", False)

car.display_info()
motorcycle.display_info()



