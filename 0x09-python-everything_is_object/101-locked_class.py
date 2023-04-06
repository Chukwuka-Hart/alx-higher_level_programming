#!/usr/bin/python3

""" Defines a LockedClass """


class LockedClass:
    """ Prevents user from dynamically creating
    new instance attributes, except if the new
    instance attribute is called 'first_name'."""

    __slots__= 'first_name'
