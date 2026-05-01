#!/usr/bin/python3
"""Defines a MyList class."""


class MyList(list):
    """Inherits from list and adds print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
