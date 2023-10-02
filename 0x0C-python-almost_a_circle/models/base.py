#!/usr/bin/python3

""" This is the defination of the base model """


class Base:
    """ This is the Base class defination

    Private attributes:
        _nb_objects = 0

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This is the initialing of the class

        Args:
            id (int): This is the identity value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
