#!/usr/bin/env python3
# bin_search1.py  UNFINISHED
# Glenn G. Chappell
# 2026-09-15
#
# Binary Search
# Implementation #1: recursive
# For CS 311 Fall 2026


import sys  # For .stdout


def bin_search(key, container, index1=None, index2=None):
    """Do Binary Search for given key in given container.
    Range to be searched is [container[index1], container[index2]),
    or the whole container if index1, index2 are not passed.
    """

    return False  # DUMMY
    # TODO: WRITE THIS!!!


def try_bin_search(key, container, expect):
    """Call bin_search(key, container), expect = expected return.
    Print results.
    """

    assert isinstance(expect, bool)

    # Do search
    print(f"Doing Binary Search for: {key}", end="")
    sys.stdout.flush()

    success = bin_search(key, data)

    # Print result
    print(f" - result: {'found' if success else 'not found'}", end="")
    if success == expect:
        print(" [correct]")
    else:
        print(" [INCORRECT] ****************************************")


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    sys.stdout.flush()
    dummy = input(msg)


# Main program
# Do several searches using binSearch. Print results.

if __name__ == "__main__":
    # Size of dataset - TRY CHANGING THIS! MUST BE GREATER THAN 100.
    DATA_SIZE = 200_000_000

    assert DATA_SIZE > 100

    # Initialize data to search
    print(f"Initializing data, DATA_SIZE = {DATA_SIZE:,} ... ", end="")
    sys.stdout.flush()

    data = list(range(0, 10*DATA_SIZE, 10))  # data is sorted

    print("DONE")
    print()

    # List of searches to do
    searches = [
        ( 10,                  True  ),  # (search key, expect success?)
        ( 1000,                True  ),
        ( (DATA_SIZE//10)*10,  True  ),
        ( (DATA_SIZE//2)*10,   True  ),
        ( (DATA_SIZE-1)*10,    True  ),
        ( 11,                  False ),
        ( (DATA_SIZE//2)*10+1, False ),
        ( -10,                 False ),
        ( DATA_SIZE*10,        False ),
    ]

    # Wait for user before Binary Search calls
    user_pause("Press ENTER for Binary Search calls ")
    print()

    # Do Binary Search calls
    for key, expect in searches:
        try_bin_search(key, data, expect)

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

