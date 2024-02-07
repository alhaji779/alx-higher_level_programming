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
        """Checks if the value passed is an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ New class from Base Geometry """
    def __init__(self, width, height):
        """ Initialize the Class """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ method to compute area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print default """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """ A square class inheriting from Rectangle """
    def __init__(self, size):
        """ Initilizing the square class """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ Method to calculate area of square """
        return self.__size ** 2
