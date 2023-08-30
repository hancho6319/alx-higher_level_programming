#!/usr/bin/python3
""" Defination of the class square """


class Square:
    """ Represent a square """

    def ___init___(self, size):
        """ Initializing a new square

        Args:
            size (int): This is the size of the new square
        """
        self.size = size

    @property
    def size(self):
        """ get the current size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the current area of the square """
        return (self.__size * self.__size)

    def my_print(self):
        """ Print the square with the n character """
        for i in range(0, self.__size):
            [print('#', end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
