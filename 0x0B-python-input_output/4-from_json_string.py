#!/usr/bin/python3
import json
"""This module contains the from_json_string function"""


def from_json_string(my_str):
    """This function returns an object (Python data structure)
        represented by a JSON string"""
    return json.load(my_str)
