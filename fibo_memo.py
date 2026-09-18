#!/usr/bin/env python3
# fibo_memo.py
# Glenn G. Chappell
# 2026-09-17
"""Computing Fibonacci numbers: recursive memoizing.
For CS 311 Fall 2026
"""


import sys  # For .stdout


def fibo_helper(n, memos):
    """Nonneg int n, memos (list) -> F(n), the nth Fibonacci number.
    F(0) = 0. F(1) = 1. For k >= 2, F(k) = F(k-2) + F(k-1).
    Uses precomputed values in memos (memos[k] is either None or F(k)).
    Records any computed values in memos.

    Pre:
    * isinstance(n, int).
    * n >= 0.
    * isinstance(memos, list).
    * n < len(memos).
    * For each k in [0, len(memos)),
      * memos[k] is either None or F(k).
    """

    assert isinstance(n, int)
    assert n >= 0
    assert isinstance(memos, list)
    assert n < len(memos)

    if memos[n] is None:
        # Compute F(n) and store it in memos

        if n <= 1:  # BASE CASE
            result = n
        else:       # RECURSIVE CASE
            result = fibo_helper(n-2, memos) + fibo_helper(n-1, memos)

        memos[n] = result

    assert isinstance(memos[n], int)
    return memos[n]


def fibo(n):
    """Nonneg int n -> F(n), the nth Fibonacci no.
    F(0) = 0. F(1) = 1. For k >= 2, F(k) = F(k-2) + F(k-1).
    Uses fibo_helper.

    Pre:
    * isinstance(n, int).
    * n >= 0.
    """

    assert isinstance(n, int)
    assert n >= 0

    memos = [None] * (n+1)
    return fibo_helper(n, memos)


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

