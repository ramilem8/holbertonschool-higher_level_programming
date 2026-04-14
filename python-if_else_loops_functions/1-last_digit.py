#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Son rakamı hesapla
if number >= 0:
    last_digit = number % 10
else:
    # Negatif sayılar için son rakamı eksi işaretli al
    last_digit = ((number * -1) % 10) * -1

# Çıktı formatını oluştur
print("Last digit of {} is {}".format(number, last_digit), end=" ")

# Koşulları kontrol et
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
