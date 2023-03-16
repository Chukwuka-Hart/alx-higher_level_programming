#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':

    count = len(argv) - 1

    if count == 3:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])

        if operator == '+':
            cal = add(a, b)
            print("{} + {} = {}" .format(a, b, cal))
            exit(0)
        elif operator == '-':
            cal = sub(a, b)
            print("{} - {} = {}" .format(a, b, cal))
            exit(0)
        elif operator == '*':
            cal = mul(a, b)
            print("{} * {} = {}" .format(a, b, cal))
            exit(0)
        elif operator == '/':
            cal = div(a, b)
            print("{} / {} = {}" .format(a, b, cal))
            exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
