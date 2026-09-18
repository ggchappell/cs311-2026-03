#!/usr/bin/env python3
# fibo_superfast.py
# Glenn G. Chappell
# 2026-09-17
"""Computing Fibonacci Numbers: super-fast method.
For CS 311 Fall 2026
"""


import sys  # For .exit


def fibo_pair(n):
    """Nonneg int n -> (F(n-1), F(n)); F(k) is kth Fibo.
    F(0) = 0. F(1) = 1. For k >= 2, F(k) = F(k-2) + F(k-1).
    Recursive. Values computed using fast method, involving a
    logarithmic number of multiplications.

    Pre:
    * isinstance(n, int).
    * n >= 0.
    """

    assert isinstance(n, int)
    assert n >= 0

    # BASE CASE

    # For n = 0: (F(-1), F(0))
    if n == 0:
        return (1, 0)

    # RECURSIVE CASE

    # Get a = F(n//2-1), b = F(n//2).
    a, b = fibo_pair(n // 2)

    # We use the following two facts:
    # * F(2k-1) = F(k-1)F(k-1) + F(k)F(k).
    # * F(2k) = 2F(k-1)F(k) + F(k)F(k).
    # Set k = n//2. Note that a is F(n//2-1); b is F(n//2).
    s = a*a
    t = a*b*2
    u = b*b
    x = s+u
    y = t+u
    # Now x is F((n//2)*2-1); y is F((n//2)*2).

    if n % 2 == 0:
        return (x, y)    # x & y are what we want
    else:
        return (y, x+y)  # Advance the pair (x, y) by one


def fibo(n):
    """Nonneg int n -> F(n), the nth Fibonacci no.
    F(0) = 0. F(1) = 1. For k >= 2, F(k) = F(k-2) + F(k-1).
    Uses fibo_pair.

    Pre:
    * isinstance(n, int).
    * n >= 0.
    """

    assert isinstance(n, int)
    assert n >= 0

    prev, curr = fibo_pair(n)
    return curr


def print_results(n):
    """Compute Fibonacci number F(n); print in pretty form."""

    print(f"F({n}) = {fibo(n)}")


def set_conversion_digits():
    """Ensure that large integers can be printed."""

    # Allow for integers with 1 billion digits.
    digits_needed = 1000000000
    if sys.get_int_max_str_digits() < digits_needed:
        sys.set_int_max_str_digits(digits_needed)


# Main program

if __name__ == "__main__":
    set_conversion_digits()  # Make sure we can print large integers

    while True:
        print()
        print("Given integer n, I will compute Fibonacci number F(n).")
        print()
        try:
            line = input("Type n [blank line to exit]: ")
            if line == "": break
            n = int(line)
            if n < 0: raise Exception()
        except:
            print()
            print("Please type a nonnegative integer")
        else:
            print()
            print_results(n)
        print()
        print("-" * 60)
    print()

