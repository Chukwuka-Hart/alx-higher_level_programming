#!/usr/bin/python3
""" Square Class """


class Square:
    """ square class """
    def __init__(self, size=0):
        """ __init__ method initializes the value

        Attribute:
                size: the size of square

        Raises:
            TypeError: if 'size' type is not an 'int'

            ValueError: if 'size' is less than '0'

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Returns the current square area """
        return self.__size ** 2
