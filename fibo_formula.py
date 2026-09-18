#!/usr/bin/env python3
# fibo_formula.py
# Glenn G. Chappell
# 2026-09-17
"""Computing Fibonacci numbers: formula.
For CS 311 Fall 2026
"""


import sys   # For .stdout
import math  # For .sqrt


def fibo(n):
    """Nonneg int n -> F(n), the nth Fibonacci no.
    F(0) = 0. F(1) = 1. For k >= 2, F(k) = F(k-2) + F(k-1).
    Uses floating-point formula.

    Pre:
    * isinstance(n, int)
    * n >= 0
    * Python's floating-point computation gives accurate results for
       this n. On my (GGC) system, this requires n <= 70.
    """

    assert isinstance(n, int)
    assert n >= 0

    sqrt5 = math.sqrt(5.0)
    phi = (1.0 + sqrt5) / 2.0
    near_fibo = pow(phi, n) / sqrt5

    # Our Fibonacci number is the nearest integer
    return round(near_fibo)


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    sys.stdout.flush()
    dummy = input(msg)


# Main program
# Print some Fibonacci numbers. Uses fibo.

if __name__ == "__main__":
    HOW_MANY_TO_PRINT = 1+70  # Number of Fibonacci numbers to print
    # Above is not 100 because of the limited precision of
    # floating-point computation.

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

