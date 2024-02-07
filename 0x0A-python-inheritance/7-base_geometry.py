#!/usr/bin/python3
"""basegeometryclass"""


class BaseGeometry:
    """instance of geometry class"""
    def __init__(self):
        """initialize class"""
        pass

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This method is to validate the value arg as integer """
        self.name = name

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        else:
            self.value = value
