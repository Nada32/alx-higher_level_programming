#!/usr/bin/python3
def uniq_add(my_list=[]):
    z = 0
    y = 0
    for i in my_list:
        for j in range(len(my_list)):
            if i != my_list[j]:
                z = z + i
                y = y + z
        return (y)
