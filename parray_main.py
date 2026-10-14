#!/usr/bin/env python3
# parray_main.py
# Glenn G. Chappell
# 2026-10-13
"""Simple main program for class PArray
For CS 311 Fall 2026
"""


import parray  # For .PArray


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    print("", end="", flush=True)
    _ = input(msg)


# Main program
# Uses simple functionality from class PArray

if __name__ == "__main__":

    print("Using class PArray")
    print()

    p1 = parray.PArray([2, 7, 4, 6, 3, 7, 3, 1])
    print(f"Initial data: {p1}")

    ix = 3
    print(f"Item #{ix}: {p1[ix]}")

    ix = 2
    val = 9999
    p1[ix] = val
    print(f"Item #{ix} set to {val}: {p1}")

    p1.sort()
    print(f"Sorted: {p1}")

    p1.sort(reverse=True)
    print(f"Reverse sorted: {p1}")

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

