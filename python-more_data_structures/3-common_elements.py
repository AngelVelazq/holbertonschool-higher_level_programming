#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()  # Step 1: Initialize an empty set
    for element in set_1:  # Step 2: Iterate through set 1
        if element in set_2:  # Step 3: Check for common elements
            common_set.add(element)  # Step 4: Add common element to the set
    return common_set  # Step 5: Return the set of common elements
