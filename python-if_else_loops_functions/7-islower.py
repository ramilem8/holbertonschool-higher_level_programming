#!/usr/bin/python3
def islower(c):
    """Karakterin küçük harf olup olmadığını kontrol eden fonksiyon."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False