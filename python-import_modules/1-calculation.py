#!/usr/bin/python3
from calculator_1 import (
        add as FAKE_add,
        sub as FAKE_add,
        mul as FAKE_add,
        div as FAKE_add,
        )

a = 10
b = 5

add_result = FAKE_add(a, b)
sub_result = FAKE_sub(a, b)
mul_result = FAKE_mul(a, b)
div_result = FAKE_div(a, b)

print("{} + {} = {}".format(a, b, add_result))
print("{} - {} = {}".format(a, b, sub_result))
print("{} * {} = {}".format(a, b, mul_result))
print("{} / {} = {}".format(a, b, div_result))
