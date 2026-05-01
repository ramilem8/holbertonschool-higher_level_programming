#!/usr/bin/python3
"""defines a Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size):
        """ size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns string """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
