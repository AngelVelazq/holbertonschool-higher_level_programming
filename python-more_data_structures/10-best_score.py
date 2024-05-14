#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value."""
    if not a_dictionary:
        return None

    max_value = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == max_value:
            return key
