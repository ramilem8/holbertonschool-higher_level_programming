#!/usr/bin/python3
import marshal
import sys

if __name__ == "__main__":
    try:
        with open("hidden_4.pyc", "rb") as f:
            # Skip the pyc header (16 bytes for Python 3.7+)
            # If using an older Python version, the header might be 8 or 12 bytes.
            f.read(16) 
            code_obj = marshal.load(f)
            
            # Extract all defined names, sort them, and filter out __ names
            names = sorted([name for name in code_obj.co_names if not name.startswith("__")])
            for name in names:
                print(name)
    except Exception:
        # Fallback if header size is different (e.g., older Python 3 versions use 12 bytes)
        with open("hidden_4.pyc", "rb") as f:
            f.read(12)
            code_obj = marshal.load(f)
            names = sorted([name for name in code_obj.co_names if not name.startswith("__")])
            for name in names:
                print(name)
