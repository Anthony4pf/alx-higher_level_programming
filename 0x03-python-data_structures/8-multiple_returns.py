#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]

    len_str = len(sentence)

    new_tuple = (len_str, first_char)

    return new_tuple
