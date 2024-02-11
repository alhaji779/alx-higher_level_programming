#!/usr/bin/python3
""" Almost a circle project """


class Base:
    """ Base module """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing the base module """
        self.id = id

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
