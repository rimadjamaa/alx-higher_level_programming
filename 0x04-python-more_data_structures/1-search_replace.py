#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    Args:
        my_list: The initial list.
        search: The element to replace in the list.
        replace: The new element.

    Returns:
        A new list with all occurrences of 'search' replaced by 'replace'.
    """
    # Create a new list to store the result
    new_list = []

    # Iterate over each element in the input list
    for elem in my_list:
        # Replace 'search' with 'replace' if the element matches 'search'
        if elem == search:
            new_list.append(replace)
        else:
            new_list.append(elem)

    return new_list
