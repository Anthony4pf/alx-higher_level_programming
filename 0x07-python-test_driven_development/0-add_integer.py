#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """Returns the sum of two numbers
    Args:
        a (int, float): first number
        b (int, float): second number
    Returns: sum of the numbers
    """
    if type(a) in (int, float) and type(b) in (int, float):
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
        return a + b
    else:
        if type(a) not in (int, float):
            raise TypeError("a must be an integer")
        if type(b) not in (int, float):
            raise TypeError("b must be an integer")
