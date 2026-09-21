#!/usr/bin/env python3
# bin_search3.py
# Glenn G. Chappell
# 2026-09-21
"""Binary Search: single tail-recursive call
Based on bin_search2.py
For CS 311 Fall 2026
"""


import sys  # For .stdout


def bin_search(key, container, index1=None, index2=None):
    """Do Binary Search for given key in given container.
    Range to be searched is [container[index1], container[index2]),
    or the whole container if index1, index2 are not passed.

    Pre:
    * If index1, index2 are both given, then:
      * index1 and index2 have type int.
      * index1 <= index2.
      * Integers in [index1, index2) are valid indices for container.
    * Values in container[index1 .. index2-1], or in whole container
      if index1, index2 not given, are sorted ascending by <.
    """

    if index1 is None:
        index1 = 0
    assert isinstance(index1, int)
    if index2 is None:
        index2 = len(container)
    assert isinstance(index2, int)
    assert index2 >= index1

    # Compute size of range ONCE
    size = index2 - index1

    # BASE CASE

    if size <= 1:
        if size == 0:      # Range has size 0
            return False
        return (not(container[index1] < key) and
               not(key < container[index1]))
            # Range has size 1; check equivalence

    # RECURSIVE CASE

    # Compute index of pivot: item in middle position of range
    pivot_index = index1 + size // 2

    if key < container[pivot_index]:
        # Recursively search first half of range
        #return bin_search(key, container, index1, pivot_index)
        index2 = pivot_index
    else:
        # Recursively search second half of range
        #return bin_search(key, container, pivot_index, index2)
        index1 = pivot_index

    # Single tail-recursive call
    return bin_search(key, container, index1, index2)


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

