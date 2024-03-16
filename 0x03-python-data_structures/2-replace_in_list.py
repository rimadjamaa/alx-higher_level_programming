#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # If the index is negative or out of range, return the original list unchanged
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        # Replace the element at the specified index with the new element
        my_list[idx] = element
        return my_list
