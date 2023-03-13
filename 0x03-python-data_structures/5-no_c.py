#!/usr/bin/python3
def no_c(my_string):

    s = ''

    for i in my_string:
        if i != 'C' and i != 'c':
            s += i

    return s
