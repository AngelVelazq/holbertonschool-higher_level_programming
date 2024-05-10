#!/usr/bin/python3
from 0-add import add as FAKE_add

a = 1
b = 2

# Print the result using string formatting
print("a = {} and b = {} FAKE add() => {}".format(a, b, FAKE_add(a, b)))

if __name__ == "__main__":
    pass
