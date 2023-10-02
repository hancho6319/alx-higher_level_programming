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
        Raaise:
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """ This is to make able of get and set for the width attribute """
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
