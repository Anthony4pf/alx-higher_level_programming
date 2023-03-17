#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    i = 0
    for key, value in a_dictionary.items():
        if (i == 0):
            best_key = key
            best_value = value
        if value > best_value:
            best_value = value
            best_key = key
        i = 1
    return best_key
