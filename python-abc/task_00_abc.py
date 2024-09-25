#!/usr/bin/env python3
from abc import ABC, abstractmethod

# Definimi i klasës abstrakte Animal
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Definimi i klasës Dog që trashëgon nga Animal
class Dog(Animal):
    def sound(self):
        return "Bark"

# Definimi i klasës Cat që trashëgon nga Animal
class Cat(Animal):
    def sound(self):
        return "Meow"
