#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    z = []
    for i in range(len(my_list)):
        if i == idx:
            my_list.remove(my_list[idx])
    return (my_list)
