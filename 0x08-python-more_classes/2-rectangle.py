#!/usr/bin/python3
""" A module to build Rectangles """



class Rectangle:
    """ This is a Rectangle building class
    """
    
    def __init__(self, width=0, height=0):
        """ The initialisation of the Rectangle class
        """

        self.width = width
        self.height = height
    
    @property
    def width(self):
        """ The width of the rectangle 
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ The value setter for width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ The height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ The value setter for height
        
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


    def area(self):
        """ Method to calculate area of rectangle
        given width and height
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Metthod to calculate perimeter of rectangle
        given width and height
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            peri = self.__width + self.__height
            return 2 * peri
