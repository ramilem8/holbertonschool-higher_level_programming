#!/usr/bin/python3
"Module that converts JSON string to Python object"
import json


def load_from_json_file(filename):
    "create a json file"
    with open(filename, "r", encoding="utf-8")as f:
        return json.load(f)