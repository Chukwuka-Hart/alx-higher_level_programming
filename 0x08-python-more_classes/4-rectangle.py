#!/usr/bin/python3
""" An empty Rectangle """


class Rectangle:
    """ A Rectangle class """
    def __init__(self, width=0, height=0):
        """ Checks the parameter and initializes a value

        Args:
            width(int): width of the rectangle.
            height(int): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of  the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Returns string with the representation of a Rectangle """
        rectangle_str = ""
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return rectangle_str

        for i in range(h):
            for j in range(w):
                rectangle_str += '#'

            if i != h - 1:
                rectangle_str += '\n'

        return rectangle_str

    def __repr__(self):
        """ Returns the representation of a Rectangle. """
        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return 'Rectangle(' + w + ', ' + h + ')'
