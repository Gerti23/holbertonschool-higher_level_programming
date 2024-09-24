#!/usr/bin/python3
"""
Module: base_geometry

This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class:

    A base class for geometric operations.
    """
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be greater than 0")
