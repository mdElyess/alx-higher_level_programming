#!/usr/bin/python3

def element_at(my_list, idx):
    l = len(my_list)

    if idx not in range(l):
        return None

    return my_list[idx]
