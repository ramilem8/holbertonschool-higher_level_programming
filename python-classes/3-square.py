#!/usr/bin/python3
"""This module defines a square class."""


class Square:
    """Square class with size validation and area calculation."""

    def __init__(self, size=0):
        """Initialize square with size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2