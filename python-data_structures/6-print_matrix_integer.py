#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate over each row in the matrix
    for row in matrix:
        # Iterate over each element in the row
        for i in range(len(row)):
            # Print the element followed by a space
            print("{:d}".format(row[i]), end="")
            # Print a space after each element, except for the last one
            if i != len(row) - 1:
                print(" ", end="")
        # Move to the next line after printing each row
        print()
