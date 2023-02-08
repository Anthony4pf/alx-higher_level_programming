#!/usr/bin/python3
"""This module contains a function that creates
an Onject from a JSON text file
"""
import json


def load_from_json_file(filename):
    """create an Object from a JSON file"""
    with open(filename, "r" encoding="utf-8") as f:
        return json.load(f)
