#!/usr/bin/python3
import sys

if __name__ == '__main__':
    s = sys.argv
    c = len(s) - 1

    if c == 0:
        print("0 arguments.")
    elif c == 1:
        print("1 argument:")
    else:
        print("{} arguments:" .format(c))

    for i in range(1, c + 1):
        print("{}: {}" .format(i, s[i]))
