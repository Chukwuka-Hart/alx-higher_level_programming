#!/usr/bin/python3
def fizzbuzz():
    for fb in range(1, 101):
        if fb % 3 == 0 and fb % 5 == 0:
            print("FizzBuzz ", end='')
            continue
        elif fb % 3 == 0:
            print("Fizz ", end='')
            continue
        elif fb % 5 == 0:
            print("Buzz ", end='')
            continue
        else:
            print("{}".format(fb), end=" ")
