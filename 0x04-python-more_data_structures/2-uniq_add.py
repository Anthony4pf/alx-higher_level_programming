#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_add = 0

    for num in set(my_list):
        sum_add += num

    return sum_add
