#!/usr/bin/python3
import sys

if __name__ == '__main__':

    s = sys.argv
    c = len(s)
    sum = 0

    if c > 1:
        for i in range(1, c):
            sum += int(s[i])

    print(sum)
