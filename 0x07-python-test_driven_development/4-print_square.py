#!/usr/bin/python3
"""This module contains a function that prints a square"""


def print_square(size):
    """prints a square with the character #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for i in range(size):
            for x in range(size):
                print("#", end="")
            print()
