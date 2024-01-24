#!/usr/bin/python3
"""class Square definition"""


class Square:
    """
    Class that defines properties of square by: (based on 1-square.py).

    Attributes:
        size: size of a square (1 side).
        raise exceptions given certain conditions
    """
    def __init__(self, size=0):
        """Creates new instances of square (1 side).

        Args:
            size: size of the square.
        """

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif (self.__size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


    def area(self):
        """ Function to calculate area of square.

        """
        return (self.__size ** 2)
