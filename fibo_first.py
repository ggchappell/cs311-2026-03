#!/usr/bin/env python3
# fibo_first.py
# Glenn G. Chappell
# Started: 2026-09-13
# Updated: 2026-09-14
"""Computing Fibonacci numbers: slow recursive.
For CS 311 Fall 2026
"""


import sys  # for .stdout


def fibo(n):
    """Given nonnegative int n, returns F(n).

    Pre:
        isinstance(n, int)
        n >= 0
    """

    assert isinstance(n, int)
    assert n >= 0

    # BASE CASE

    # Invariant: n >= 0
    assert n >= 0
    if n <= 1:
        return n

    # RECURSIVE CASE

    # Invariant: n >= 2
    assert n >= 2
    return fibo(n-2) + fibo(n-1)


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

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

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

