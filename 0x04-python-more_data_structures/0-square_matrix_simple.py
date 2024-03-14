#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
        matrix: A 2 dimensional array.

    Returns:
        A new matrix with each value being the square of the corresponding value in the input matrix.
    """
    # Create a new matrix to store the result
    result_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Create a new row to store the squared values
        squared_row = []
        # Iterate over each element in the row and compute its square
        for num in row:
            squared_row.append(num ** 2)
        # Add the squared row to the result matrix
        result_matrix.append(squared_row)

    return result_matrix
