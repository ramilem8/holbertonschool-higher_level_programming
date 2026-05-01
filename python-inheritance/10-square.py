#!/usr/bin/python3
"""defies a Square class"""
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """ inherits from Rectangle"""

    def __init__(self, size):
        """ size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size