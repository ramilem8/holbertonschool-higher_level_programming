#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    # Perform and print results in a minimal number of print statements
    results = [
        "{} + {} = {}".format(a, b, add(a, b)),
        "{} - {} = {}".format(a, b, sub(a, b)),
        "{} * {} = {}".format(a, b, mul(a, b)),
        "{} / {} = {}".format(a, b, div(a, b))
    ]
    
    # Loop to print all results using only 4 print statements
    for result in results:
        print(result)