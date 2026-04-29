#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """Rectangle class with area, perimeter and printable output."""

    def __init__(self, width=0, height=0):
        """Initialize rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return printable rectangle with #."""
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []
        for _ in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)

    def __repr__(self):
        """Return official representation of rectangle."""
        return "<3-rectangle.Rectangle object at {}>".format(hex(id(self)))
