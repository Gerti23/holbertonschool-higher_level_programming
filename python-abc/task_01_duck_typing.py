from abc import ABC, abstractmethod

# Define the abstract class Shape
class Shape(ABC):
    """
    Abstract base class for different shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        This method must be implemented by subclasses.
        """
        pass

# Circle class inheriting from Shape
class Circle(Shape):
    """
    Circle class that implements the Shape interface.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.
        :param radius: Radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        :return: Area of the circle
        """
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.
        :return: Perimeter of the circle
        """
        return 2 * 3.14159 * self.radius

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    """
    Rectangle class that implements the Shape interface.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with a given width and height.
        :param width: Width of the rectangle
        :param height: Height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        :return: Area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        :return: Perimeter of the rectangle
        """
        return 2 * (self.width + self.height)

# Function to print area and perimeter of a shape
def shape_info(shape):
    """
    Print the area and perimeter of a shape.
    This function relies on duck typing and does not check the type of the shape.
    :param shape: An object that implements the Shape interface
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Testing the classes and function
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    shape_info(circle)
    shape_info(rectangle)
