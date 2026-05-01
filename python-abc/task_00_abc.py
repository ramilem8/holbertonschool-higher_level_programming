#!/usr/bin/env python3
"""Module demonstrating abstract base classes"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class Animal"""

    @abstractmethod
    def sound(self):
        """Method that must be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog class"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class"""

    def sound(self):
        return "Meow"
