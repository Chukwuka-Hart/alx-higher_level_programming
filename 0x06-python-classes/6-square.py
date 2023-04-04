#!/usr/bin/python3
""" Square Class """


class Square:
    """ square class """
    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ Returns the current square area """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return None
        elif self.__position != 0:
            for h in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print('')
