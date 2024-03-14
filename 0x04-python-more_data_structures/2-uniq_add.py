#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Convert the list to a set to remove duplicates
    unique_set = set(my_list)
    # Sum up the unique integers
    result = sum(unique_set)
    return result
