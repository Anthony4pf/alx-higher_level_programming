#!/usr/bin/python3
"""This module contains the is_subclass_of function"""


def inherits_from(obj, a_class):
    """This function checks if an object is a subclass of a class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
