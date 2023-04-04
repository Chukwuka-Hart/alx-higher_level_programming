#!/usr/bin/python3
def safe_print_division(a, b):
    divide = 0

    try:
        divide = a / b
    except ZeroDivisionError:
        divide = None
    finally:
        print("Inside result: {}".format(divide))
        return divide
