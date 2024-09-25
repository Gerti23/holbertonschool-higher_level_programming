#!/usr/bin/python3
"""
This line indicates that the script should be executed using Python 3.
It is known as a shebang line and helps the operating system determine
which interpreter to use to run the script.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract class representing a geometric shape.
    This class cannot be instantiated and contains two abstract methods: 'area' and 'perimeter'.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method that must be implemented by subclasses.
        This method should return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method that must be implemented by subclasses.
        This method should return the perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    Class representing a circle, inheriting from the Shape class.
    Implements the 'area' and 'perimeter' methods.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        """
        Returns the perimeter (circumference) of the circle.
        """
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    """
    Class representing a rectangle, inheriting from the Shape class.
    Implements the 'area' and 'perimeter' methods.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def shape_info(shape):
        
    """
    Function that takes a shape object and prints its area and perimeter.
    Relies on duck typing to call the 'area' and 'perimeter' methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    
    print("Circle Info:")
    shape_info(circle)  # Output: Area: 78.5, Perimeter: 31.400000000000002
    
    print("\nRectangle Info:")
    shape_info(rectangle)  # Output: Area: 24, Perimeter: 20
