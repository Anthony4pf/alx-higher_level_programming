#!/usr/bin/python3
"""THis module contains the square class"""


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialises Square(overrides Rectangle init)"""
        super.__init__(size, size, x, y, id)

    def __str__(self):
        """Str function of square"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)
