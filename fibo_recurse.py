#!/usr/bin/env python3
# fibo_recurse.py
# Glenn G. Chappell
# Started: 2026-09-17
# Updated: 2026-09-18
"""Computing Fibonacci numbers: fast recursive..
For CS 311 Fall 2026
"""


import sys  # For .stdout


def fibo_pair(n):
    """Nonneg int n -> (F(n-1), F(n)); F(k) is kth Fibo.
    F(0) = 0. F(1) = 1. For k >= 2, F(k) = F(k-2) + F(k-1).
    Uses recursive method, returning a pair.

    Pre:
    * isinstance(n, int).
    * n >= 0.
    """

    # BASE CASE

    if n == 0:
        return ( 1, 0 )

    # RECURSIVE CASE

    prev, curr = fibo_pair(n-1)
    return ( curr, prev+curr )


def fibo(n):
    """Nonneg int n -> F(n), the nth Fibonacci no.
    F(0) = 0. F(1) = 1. For k >= 2, F(k) = F(k-2) + F(k-1).
    Uses fibo_pair.

    Pre:
    * isinstance(n, int)
    * n >= 0
    """

    assert isinstance(n, int)
    assert n >= 0

    prev, curr = fibo_pair(n)
    return curr


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

