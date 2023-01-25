#!/usr/bin/python3
"""Square Class Definition"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.size = size

    @property
    def size(self):
        """Retrive the value of the side of a square
        Returns: side of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Set the value of the side of a square
        Args:
            size (int): size of the square
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of a square
        Returns: area of the square
        """
        return self.size ** 2
