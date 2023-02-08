#!/usr/bin/python3
"""This module contains the read_file() function"""


def read_file(filename=""):
    """This function reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
