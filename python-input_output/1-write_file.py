#!/usr/bin/python3
"""Module that writes a string to a file"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)