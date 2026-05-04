#!/usr/bin/python3
"""Module that reads a file and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")