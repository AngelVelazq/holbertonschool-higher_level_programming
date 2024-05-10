#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Skip the first argument, which is the script name itself
    args = sys.argv[1:]

    # Initialize the sum to 0
    total = 0

    # Iterate over each argument; add to total after conerting it to an integer
    for arg in args:
        total += int(arg)

    # Print the total
    print(total)
