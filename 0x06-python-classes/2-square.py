#!/usr/bin/python3
""" Defunation of a class Square """


class Square:
    """ Representation of a Square """

    def __init__(self, size=0):
        """ Initialization of a new Square.

        Args:
            size (int): This is the size of the new Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
