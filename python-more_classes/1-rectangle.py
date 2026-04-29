#!/usr/bin/python3
"""This module defines a Rectangle class"""


class Rectangle:
    """Rectangle class with width and height validation"""

    def __init__(self,width=0, height=0):
        """Initialize rectangle with width and height"""
        self.width=width
        self.height = height

    @property

def width (self):
    """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self,value):
        """Set the width with validation"""
        if not isinstance(value,int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self ._width=value

    @property
    def height (self):
        """Retrieve the height"""
        return self.__height

    @height.setter    
    def height (self,value)
    """set the height with validation"""
    if not isinstance(value,int):
        raise TYpeError("Height must be integer")
    if value <0:
        raise ValueError ("height must be >=0")
    self .__height=value
