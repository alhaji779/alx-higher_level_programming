#!/usr/bin/python3
""" Custom class to reverse == and != """

class MyInt(int):
    """ Custom myint class """
    def __init__(self, num):
        """ Initilising myint class"""
        self.num = num

    def __eq__(self, a):
        """ inverting equals to sign """
        return self.num != a

    def __ne__(self, a):
        """ inverting not equal to sign """
        return self.num == a
