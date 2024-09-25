#!/usr/bin/python3
"""
This line indicates that the script should be executed using Python 3.
It is known as a shebang line and helps the operating system determine
which interpreter to use to run the script.
"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract class representing an animal.
    This class cannot be instantiated and contains an abstract method 'sound'.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        This method should return a string representing the sound of the animal.
        """
        pass

class Dog(Animal):
    """
    Class representing a dog, inheriting from the Animal class.
    Implements the 'sound' method to return the sound of a dog.
    """

    def sound(self):
        """
        Returns the sound of a dog.
        """
        return "Bark"

class Cat(Animal):
    """
    Class representing a cat, inheriting from the Animal class.
    Implements the 'sound' method to return the sound of a cat.
    """

    def sound(self):
        """
        Returns the sound of a cat.
        """
        return "Meow"
