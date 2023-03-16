#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    photocopied_dict = a_dictionary.copy()

    for key, value in photocopied_dict.items():
        photocopied_dict[key] = value * 2

    return photocopied_dict
