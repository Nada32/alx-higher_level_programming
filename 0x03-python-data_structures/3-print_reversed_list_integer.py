#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    z = my_list
    for i in range(len(my_list)):

        z[len(my_list) - i] = my_list[i]
    return z
