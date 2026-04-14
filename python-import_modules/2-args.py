#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Skriptin adı çıxılmaqla arqumentlərin sayı
    count = len(sys.argv) - 1

    # İlk sətrin formatlanması
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Hər bir arqumentin mövqeyi və dəyəri
    for i in range(1, count + 1):
        print("{}: {}".format(i, sys.argv[i]))