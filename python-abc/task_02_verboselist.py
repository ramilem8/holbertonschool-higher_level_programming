#!/usr/bin/env python3
"""Module for VerboseList"""

class VerboseList(list):
    """List that prints messages on modifications"""

    def append(self, item):
        """Add item and print message"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print message"""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove item and print message"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item and print message"""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)