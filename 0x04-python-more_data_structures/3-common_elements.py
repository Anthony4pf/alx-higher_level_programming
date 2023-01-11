#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = []
    for elem in set(set_1):
        for index in set(set_2):
            if elem == index:
                new_set.append(elem)

    return (new_set)
