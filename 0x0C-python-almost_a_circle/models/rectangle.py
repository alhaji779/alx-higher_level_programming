#!/usr/bin/python3
""" Class Rectangle """


from models.base import Base

class Rectangle(Base):
    """ Rectangle class inheriting from base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialising Rectangle class """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)


    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height


    @height.setter
    def height(self, value):
        """ setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter of x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value


    def area(self):
        """ calculate area of rectangle """
        return self.__width * self.__height


    def display(self):
        """ function to display class instance """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print()


    def __str__(self):
        """ default print of class rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ function to update from screen """
        if args and len(args) != 0:
            self.id = args[0] if len(args) >= 1 else self.id
            self.__width = args[1] if len(args) >= 2 else self.__width
            self.__height = args[2] if len(args) >= 3 else self.__height
            self.__x = args[3] if len(args) >= 4 else self.__x
            self.__y = args[4] if len(args) >= 5 else self.__
        if kwargs:
            self.id = kwargs.get('id', self.id)
            self.__width = kwargs.get('width', self.__width)
            self.__height = kwargs.get('height', self.__height)
            self.__x = kwargs.get('x', self.__x)
            self.__y = kwargs.get('y', self.__y)
