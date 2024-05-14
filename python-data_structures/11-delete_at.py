#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        # Return the same list if idx is invalid
        return my_list

    # Create a new list containing elements before idx
    result = my_list[:idx]

    # Extend the new list with elements after idx
    result.extend(my_list[idx + 1:])

    return result
