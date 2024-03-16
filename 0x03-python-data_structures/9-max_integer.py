#!/usr/bin/python3

def max_integer(my_list=[]):
    # If the list is empty, return None
    if not my_list:
        return None
    # Initialize max_value with the first element of the list
    max_value = my_list[0]
    # Iterate through the list starting from the second element
    for num in my_list[1:]:
        # Update max_value if the current number is greater
        if num > max_value:
            max_value = num
    return max_value
