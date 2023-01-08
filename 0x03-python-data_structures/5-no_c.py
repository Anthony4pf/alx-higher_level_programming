#!/usr/bin/python3
def no_c(my_string):
    new_string = ""

    for i, char in enumerate(my_string):
        if char != 'c' and char != 'C':
            new_string += char

    return new_string
