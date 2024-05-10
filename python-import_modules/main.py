#!/usr/bin/python3
from add_0 import add as FAKE_add

a = 1
b = 2

# Print the result using string formatting
print("a = {} and b = {} FAKE add() => {}".format(a, b, FAKE_add(a, b)))
