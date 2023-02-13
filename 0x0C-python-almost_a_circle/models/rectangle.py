#!/usr/bin/python3
"""This module contains the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle whch implements Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """string representation of a rectangle instance"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    @property
    def width(self):
        """getter for the __width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the __width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for the __height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the __height attr"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x attr"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x attr"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y attr"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y attr"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle instance"""
        return (self.__width * self.__height)

    def display(self):
        """prints the to stdout the Rectangle Instance with char #"""
        print("\n" * self.__y, end="")

        for i in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:

            pass

    def to_dictionary(self):
        """
            returns the dictionary repr of a rectangle
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
