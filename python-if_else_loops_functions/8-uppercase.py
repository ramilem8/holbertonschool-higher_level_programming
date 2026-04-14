#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Karakter küçük harf ise (a-z), ASCII farkını kullanarak büyüt (a=97, A=65)
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")