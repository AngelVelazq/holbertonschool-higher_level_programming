#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_set_1 = set()  # Step 1: Initialize empty sets for unique elements
    unique_set_2 = set()
    for element in set_1:  # Step 2: Iterate through set 1
        if element not in set_2:  # Step 3: Check for uniqueness
            unique_set_1.add(element)  # Step 4: Add elements to their sets
    for element in set_2:  # Repeat steps 2-4 for set 2
        if element not in set_1:
            unique_set_2.add(element)
    return unique_set_1.union(unique_set_2)  # Step 5: Combine sets & return
