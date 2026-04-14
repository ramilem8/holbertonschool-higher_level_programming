#!/usr/bin/python3
def fizzbuzz():
    """1'den 100'e kadar FizzBuzz kurallarıyla yazdırır."""
    for i in range(1, 101):
        if i % 15 == 0:
            output = "FizzBuzz"
        elif i % 3 == 0:
            output = "Fizz"
        elif i % 5 == 0:
            output = "Buzz"
        else:
            output = "{}".format(i)

        print("{}".format(output), end=" ")
