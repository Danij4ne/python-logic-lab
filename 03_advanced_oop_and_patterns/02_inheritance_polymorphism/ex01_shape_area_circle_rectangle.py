
"""
Ex01 - Shape Area Calculator (Inheritance)

Description:
    Create a base class Shape and two subclasses: Circle and Rectangle.
    Each subclass should implement its own method to calculate area.

Requirements:
    - Define a base class named Shape.
    - Define a method calculate_area() in Shape (can be a placeholder or return 0).
    - Create a subclass Circle with:
        - a radius attribute
        - its own calculate_area() method
    - Create a subclass Rectangle with:
        - width and height attributes
        - its own calculate_area() method
    - In the main part of the script, create instances of Circle and Rectangle
      and call their calculate_area() methods.

Notes:
    - Use the formula: Circle area = π * radius^2 (π can be 3.14).
    - Rectangle area = width * height.
    - This exercise focuses on inheritance and method overriding.

Example (expected behavior):
    Circle area: 78.5
    Rectangle area: 20
"""

# TODO:
# 1. Define the Shape base class with a calculate_area() method.
# 2. Create Circle and Rectangle subclasses that override calculate_area().
# 3. Create instances and print their calculated areas.

 
class Shape:
    def calculate_area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

 
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


 
circle = Circle(5)
rectangle = Rectangle(4, 5)

print("Circle area:", circle.calculate_area())
print("Rectangle area:", rectangle.calculate_area())

