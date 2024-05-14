#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(roman_string)):
        if (i < len(roman_string) - 1 and
                roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]):
            total -= roman_dict[roman_string[i]]
        else:
            total += roman_dict[roman_string[i]]

    return total


print(roman_to_int("III"))        # Output: 3  # Test cases
print(roman_to_int("IV"))         # Output: 4
print(roman_to_int("IX"))         # Output: 9
print(roman_to_int("LVIII"))      # Output: 58
print(roman_to_int("MCMXCIV"))    # Output: 1994
print(roman_to_int(None))         # Output: 0
