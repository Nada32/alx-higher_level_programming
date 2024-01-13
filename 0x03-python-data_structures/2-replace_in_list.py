#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if idx > len(my_list) - 1:
            return (my_list)
        elif idx <= len(my_list) - 1 and idx >= 0:
            my_list[idx] = element
        elif idx < 0:
            return (my_list)
    return (my_list)
