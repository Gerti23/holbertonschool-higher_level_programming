#!/usr/bin/python3
"""
Rectangle Module

Provides a Rectangle class with width and height attributes.
"""

class Rectangle:
    """
    A class used to represent a Rectangle

    Attributes
    ----------
    width : int
        The width of the rectangle
    height : int
        The height of the rectangle

    Methods
    -------
    area() -> int:
        Returns the area of the rectangle
    perimeter() -> int:
        Returns the perimeter of the rectangle
    __str__() -> str:
        Returns a string representation of the rectangle using the '#' character
    __repr__() -> str:
        Returns a string representation of the rectangle that can be used to recreate a new instance
    """

    def __init__(self, width: int, height: int):
        """
        Parameters
        ----------
        width : int
            The width of the rectangle
        height : int
            The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value: int):
        """
        Sets the width of the rectangle

        Parameters
        ----------
        value : int
            The width of the rectangle

        Raises
        ------
        TypeError
            If the width is not an integer
        ValueError
            If the width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value: int):
        """
        Sets the height of the rectangle

        Parameters
        ----------
        value : int
            The height of the rectangle

        Raises
        ------
        TypeError
            If the height is not an integer
        ValueError
            If the height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """
        Returns the area of the rectangle

        Returns
        -------
        int
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self) -> int:
        """
        Returns the perimeter of the rectangle

        Returns
        -------
        int
            The perimeter of the rectangle, or 0 if either width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """
        Returns a string representation of the rectangle using the '#' character

        Returns
        -------
        str
            A string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self) -> str:
        """
        Returns a string representation of the rectangle that can be used to recreate a new instance

        Returns
        -------
        str
            A string representation of the rectangle
        """
        return f"Rectangle({self.width}, {self.height})"
