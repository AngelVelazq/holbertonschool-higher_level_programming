#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for item in my_list:
            if count >= x:
                break
            print(item, end=" ")
            count += 1
        print()  # Print newline after printing all elements
        return count
    except TypeError as e:
        print("TypeError:", e)
        return count
    except Exception as e:
        print("An error occurred:", e)
        return count
