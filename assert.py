#!/usr/bin/env python3
# assert.py
# Glenn G. Chappell
# 2026-08-26
"""Using assert in Python.
For CS 311 Fall 2026
"""


def max(my_list):
    """Return the maximum value in nonempty list my_list."""
    assert isinstance(my_list, list), "max: mylist must be a list"
    assert len(my_list) > 0, "max: my_list must be nonempty"

    result = my_list[0]
    for val in my_list:
        if val > result:
            result = val
    return result


# Sum a nonempty list; should work
print()
input("Press ENTER find max value in array1 (nonempty) ")
array1 = [1, 2, 3, 4]  # Nonempty array
print("Result:", max(array1))

# Sum an empty array; should crash due to failed assertion
print()
input("Press ENTER to find max value in array2 (empty) ")
array2 = []  # Empty array
print("Result:", max(array2))

