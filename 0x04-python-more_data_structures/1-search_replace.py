#!/usr/bin/python3
def search_replace(my_list, search, replace):
    z = []
    for i in my_list:
        if i == search:
            i = replace
            z.append(i)
        else:
            z.append(i)
    return (z)
