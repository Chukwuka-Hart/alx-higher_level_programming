#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0

    try:
        for i in my_list:
            if n < x:
                print('{}'.format(my_list[n]), end='')
                n += 1
    except TypeError:
        pass
    print()
    return n
