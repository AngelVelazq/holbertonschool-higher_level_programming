#!/usr/bin/python3
def print_last_digit(number):
    num = abs(number)
    last_digit = num % 10
    print(last_digit, end="")
    return last_digit
