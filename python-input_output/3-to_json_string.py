#!/usr/bin/python3
"""Module that converts an object to JSON string"""
import json

def to_json_string(my_obj):
    "returns JSON represantation of an object"
    return json.dumps(my_obj)
