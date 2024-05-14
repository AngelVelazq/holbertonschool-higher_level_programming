#!/usr/bin/python3
def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    # Initialize the maximum value as the first element of the list
    max_value = my_list[0]

    # Iterate through the list starting from the second element
    for num in my_list[1:]:
        # Update max_value if the current element is greater
        if num > max_value:
            max_value = num

    return max_value
