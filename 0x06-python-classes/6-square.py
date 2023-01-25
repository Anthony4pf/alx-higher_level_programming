#!/usr/bin/python3
"""Square Class Definition"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
        __position (tuple): coordinates of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
        Args:
            size (int): size of a side of the square
            position (tuple): coordinates of the square
        Returns: None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the value of the side of a square
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

    @property
    def position(self):
        """Retrieve the value of the coordinates of the square
        Returns: coordinates in tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value of the coordinates of a square
        Returns:None
        """
        if type(value) == tuple and len(value) == 2 and \
            type(value[0]) == int and type(value[1]) == int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculate the area of a square
        Returns: area of the square
        """
        return self.size ** 2

    def my_print(self):
        """Prints a square using the # character
        Returns: None
        """
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
