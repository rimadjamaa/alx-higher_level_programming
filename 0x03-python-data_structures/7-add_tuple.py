#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a is smaller than 2, pad it with zeros
    if len(tuple_a) < 2:
        tuple_a += (0, 0)
    # If tuple_b is smaller than 2, pad it with zeros
    if len(tuple_b) < 2:
        tuple_b += (0, 0)
    # Add the first elements of tuple_a and tuple_b
    first = tuple_a[0] + tuple_b[0]
    # Add the second elements of tuple_a and tuple_b
    second = tuple_a[1] + tuple_b[1]
    # Return a new tuple containing the sum of the elements
    return (first, second)
