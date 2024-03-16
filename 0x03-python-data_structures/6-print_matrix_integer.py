#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each element in the row
        for elem in row:
            # Print the element with a space after it, using str.format()
            print("{:d}".format(elem), end=" ")
        # Move to the next line after printing all elements in the row
        print()
