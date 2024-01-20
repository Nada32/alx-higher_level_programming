#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x=[]
    for i in range(len(my_list)):
        if idx > len(my_list) - 1:
            return (my_list)
        elif idx <= len(my_list) - 1 and idx >= 0:
            x.append(my_list[i])
        elif idx < 0:
            return (my_list)
    x[idx] = element
    return (x)
