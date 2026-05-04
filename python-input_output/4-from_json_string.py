#!/usr/bin/python3
 """Module that converts an object to JSON string"""


import json:


def from_json_string(my_str):
    "returns JSON represantation of an object"
    return json.loads(my_str)