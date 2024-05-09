#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase using ASCII values
            result += chr(ord(char) - 32)
            # ASCII values of lowercase letters are 32 greater than uppercase
        else:
            result += char
    return result


test_cases = ["holberton", "Holberton School",
              "Holberton School, 98 battery street", "",
              98, "z"]

for case in test_cases:
    if isinstance(case, str):
        print(uppercase(case))
    else:
        print("{}".format(uppercase(str(case))))
