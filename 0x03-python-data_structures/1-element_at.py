#!/usr/bin/python3
# User function to retrieve an element from a list
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
