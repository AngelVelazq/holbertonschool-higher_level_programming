#!/usr/bin/python3
"""
Unittests for max_integer function
"""

import unittest
import importlib.util
import sys

# Dynamically load the 6-max_integer module
module_name = '6-max_integer'
file_path = './6-max_integer.py'
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)
max_integer = module.max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_and_negative(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_multiple_same_max(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_list_with_strings(self):
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
