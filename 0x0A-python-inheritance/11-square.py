#!/usr/bin/python3
""" basegeometry class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class inheriting from Rectangle class """

    def __init__(self, size):
        """ initialing the square class """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """ default print of square """
        return "[Square] {}/{}".format(self.__size, self.__size)
