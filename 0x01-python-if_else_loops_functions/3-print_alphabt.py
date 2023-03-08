#!/usr/bin/python3
for alphabet in range(97, 123):
    if alphabet in [101, 113]:
        continue
    print("{}".format(chr(alphabet)), end="")
