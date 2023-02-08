#!/usr/bin/python3
"""This module contains a class MyList that inherits from list"""


class MyList(list):
    """A subclass of list"""
    def print_sorted(self):
        print(sorted(self))
