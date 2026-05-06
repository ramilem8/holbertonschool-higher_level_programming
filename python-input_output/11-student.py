#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of the instance."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {
                key: self.__dict__[key]
                for key in attrs
                if key in self.__dict__
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the instance."""
        for key, value in json.items():
            setattr(self, key, value)
