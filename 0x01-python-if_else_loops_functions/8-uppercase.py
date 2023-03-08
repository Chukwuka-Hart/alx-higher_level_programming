#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            str1 += chr((ord(letter) - 32))
        else:
            str1 += letter
    print("{}" .format(str1))
