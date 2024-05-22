#!/usr/bin/python3
"""
MyList class inherits from the built-in list class
"""


class MyList(list):
    """
    A class MyList that inherits from list.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
