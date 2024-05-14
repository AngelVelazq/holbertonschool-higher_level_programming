#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # If the key exists, update its value
        a_dictionary[key] = value
    else:
        # If the key doesn't exist, add it to the dictionary
        a_dictionary[key] = value


my_dict = {'a': 1, 'b': 2, 'c': 3}  # Test cases
update_dictionary(my_dict, 'a', 10)  # Update existing key
update_dictionary(my_dict, 'd', 4)   # Add new key
print(my_dict)  # Output: {'a': 10, 'b': 2, 'c': 3, 'd': 4}
