#!/usr/bin/python3
"""Returns the dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """Returns dictionary representation of obj."""
    return obj.__dict__
