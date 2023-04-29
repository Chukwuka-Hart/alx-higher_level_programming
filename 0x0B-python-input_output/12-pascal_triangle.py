#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    count = 1
    while count != n:
        last_ele = triangle[-1]
        tmp = [1]
        for i in range(len(last_ele) - 1):
            tmp.append(last_ele[i] + last_ele[i + 1])
        tmp.append(1)
        triangle.append(tmp)
        count += 1
    return triangle
