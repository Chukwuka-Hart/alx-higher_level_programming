#!/usr/bin/python3
for comb in range(100):
    if comb < 99:
        print("{:02d}," .format(comb, comb), end=" ")
    else:
        print(comb)
