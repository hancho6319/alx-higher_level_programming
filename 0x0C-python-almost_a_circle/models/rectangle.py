#!/usr/bin/python3

""" This is the defination of the rectangle model """
from models.base import Base


class Rectangle(Base):
    """ This is the class Rectangle defination """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is the initialization of the class Rectangle

        Args:
            width (int): This is the width value
            height (int): This is the height value
            x (int): This is the x value
            y (int): This is the y value
            id (int): This is the id value
        Raise:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ This is to make able of get and set for the width attribute """
        return self.__width

    @width.setter
    def width(self, width_value):
        """ This is the method used to set any value to the private __width """
        if not isinstance(width_value, int):
            raise TypeError("width must be an integer")
        if width_value <= 0:
            raise ValueError("width must be > 0")
        self.__width = width_value

    @width.getter
    def width(self):
        """ This is the method used to retrieve the value """
        return self.__width

    @property
    def height(self):
        """ This is the method used to make able of getter and setter """
        return self.__height

    @height.setter
    def height(self, height_value):
        """ This is the method used to set any value to the priv __height """
        if not isinstance(height_value, int):
            raise TypeError("height must be an integer")
        if height_value <= 0:
            raise ValueError("height must be > 0")
        self.__height = height_value

    @height.getter
    def height(self):
        """ This is the method used to retrieve the value of __height"""
        return self.__height

    @property
    def x(self):
        """ This is the method used to make able of getter and setter """
        return self.__x

    @x.setter
    def x(self, x_value):
        """ This is the method used to set any value to the private __x """
        if not isinstance(x_value, int):
            raise TypeError("x must be an integer")
        if x_value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = x_value

    @x.getter
    def x(self):
        """ This is the method used to retrieve the value of __x"""
        return self.__x

    @property
    def y(self):
        """ This is the method used to make able of getter and setter """
        return self.__y

    @y.setter
    def y(self, y_value):
        """ This is the method used to set any value to the private __y """
        if not isinstance(y_value, int):
            raise TypeError("y must be an integer")
        if y_value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = y_value

    @y.getter
    def y(self):
        """ This is the method used to retrieve the value of __y"""
        return self.__y
    
    def area(self):
        return self.__height * self.__width
