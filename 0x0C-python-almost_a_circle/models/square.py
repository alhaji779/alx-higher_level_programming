#!/usr/bin/python3
""" Square Class """


from models.rectangle import Rectangle
class Square(Rectangle):
    """ Square class inherit from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization of Square class """
        super().__init__(id, size, size, x, y)

    def __str__(self):
        """ Defualt print """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.__x, self.__y,  self.__size)
