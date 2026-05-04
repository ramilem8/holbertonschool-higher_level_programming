#!/usr/bin/python3
"""Module that converts JSON string to Python object"""

import json


def from_json_string(my_str):
    """Returns Python object represented by a JSON string"""
    return json.loads(my_str)
