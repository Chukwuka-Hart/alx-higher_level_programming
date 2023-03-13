#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return cpy

    cpy[idx] = element
    return cpy
