#!/usr/bin/python3

import json
import csv
import turtle

""" This is the defination of class base """


class Base:
    """ This is the Base class defination

    Args:
        _nb_objects =0

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This is the initialing of the class """
        if id is not None:
            self.id = __nb_object
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

