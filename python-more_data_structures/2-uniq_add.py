#!/usr/bin/python3
def uniq_add(the_list=[]):
    unique_integers = set()  # Step 1: Initialize an empty set
    for num in the_list:      # Step 2: Iterate through the list
        if num not in unique_integers:  # Step 3: Check for uniqueness
            unique_integers.add(num)    # Step 4: Add unique integer to the set
    return sum(unique_integers)
