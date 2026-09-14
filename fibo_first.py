#!/usr/bin/env python3
# fibo_first.py  UNFINISHED
# Glenn G. Chappell
# 2026-09-13
"""Computing Fibonacci numbers: slow recursive.
For CS 311 Fall 2026
"""


import sys  # for .stdout


def fibo(n):
    """Given nonnegative int n, returns F(n)."""

    return 42  # DUMMY
    # TODO: WRITE THIS!!!


def user_pause(msg):
    """Wait for user to press ENTER."""

    assert isinstance(msg, str)

    sys.stdout.flush()
    dummy = input(msg)


# Main program
# Print some Fibonacci numbers. Uses fibo.

if __name__ == "__main__":
    HOW_MANY_TO_PRINT = 100  # Number of Fibonacci numbers to print

    # Heading
    print("Fibonacci Numbers")
    print()

    # Print Fibonacci numbers
    for i in range(HOW_MANY_TO_PRINT):
        ff = fibo(i)
        print(f"F({i:2d}) = {ff}")  # Pad i with blanks

    print()
    user_pause("Press ENTER to quit ")

