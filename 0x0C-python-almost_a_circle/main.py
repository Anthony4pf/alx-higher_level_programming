#!/usr/bin/python3
""" 10-main """
from models.square import Square
from models.rectangle import Rectangle

if __name__ == "__main__":

    s1 = Rectangle(5, 111)
    print(s1)
    s1.height = 11
    print(s1.height)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
