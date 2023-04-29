#!/usr/bin/python3
"""Defines a function that reads text."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.
    Args:
        filename (str): The name of the file to write to.
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    print("{}".format(content), end="")
