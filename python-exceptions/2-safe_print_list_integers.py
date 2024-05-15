#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for value in my_list:
            try:
                print("{:d}".format(value))
                count += 1
                if count == x:
                    break
            except (TypeError, ValueError):
                pass
    except TypeError:
        pass
    return count
