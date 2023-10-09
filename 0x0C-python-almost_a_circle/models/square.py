#!/usr/bin/python3
""" This is the defination of square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is the defination of the square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ This is the initialization constructor of the class

        Args:
            size (int): This is the size value
            x (int): This is the x value
            y (int): This is the y value
            id (int): This is the id value
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ This is the overloading __str__ method """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """ This is the decorator used for size """
        return self.width * self.height

    @size.setter
    def size(self, widthAndHeight_value):
        """ This is the setter of the size method """
        self.height = widthAndHeight_value
        self.width = widthAndHeight_value
