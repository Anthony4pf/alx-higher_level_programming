#!/usr/bin/python3
"""This module contains  function "say_my_name"
The function prints out the full name of a person
"""


def say_my_name(first_name, last_name=""):
    """Print the full name of the person"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
