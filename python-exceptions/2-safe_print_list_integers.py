#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if count >= x:
                break
            if isinstance(item, int):
                print("{:d}".format(item), end=" ")
                count += 1
        print()  # Print newline after printing all integers
        return count
    except Exception as e:
        print("An error occurred:", e)
        return count
