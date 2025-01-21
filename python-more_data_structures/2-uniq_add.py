#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Convert the list to a set to ensure uniqueness, then sum the elements
    return sum(set(my_list))
