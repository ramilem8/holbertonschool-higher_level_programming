#!/usr/bin/python3
"""This module defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception since area is not implemented"""
        raise Exception("area() is not implemented")
