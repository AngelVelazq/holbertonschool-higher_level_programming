#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate through the input list
    for num in my_list:
        # Check if the number is divisible by 2
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    
    return result
