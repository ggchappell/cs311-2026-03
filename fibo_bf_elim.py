#!/usr/bin/env python3
# fibo_bf_elim.py
# Glenn G. Chappell
# 2026-10-25
"""Computing Fibonacci numbers: recursion eliminated (brute-force).
For CS 311 Fall 2026

This program is based on fibo_first.py.
Recursion has been eliminated using the brute-force technique covered
in class, using no algorithmic cleverness.
"""


# Original function fibo, from fibo_first.py:
#
# def fibo(n):
#     # BASE CASE
#
#     if n <= 1:
#         return n
#
#     # RECURSIVE CASE
#
#     return fibo(n-2) + fibo(n-1)
#
# Modified version used as the basis of this code:
#
# def fibo(n):
#     # BASE CASE
#
#     if n <= 1:
#         return n
#
#     # RECURSIVE CASE
#
#     r1 = fibo(n-2)  # Recursive call #1
#     r2 = fibo(n-1)  # Recursive call #2
#     return r1 + r2  # Return the result


def fibo(n):

    # Each Stack frame (class StackFrame, below) is an object with 5
    # attributes, each of type int:
    # * return_addr - our return address; possible values:
    #   * 0 - outside world (really return).
    #   * 1 - 1st recursive call.
    #   * 2 - 2nd recursive call.
    # * n - parameter.
    # * r1 - return value of 1st recursive call.
    # * r2 - return value of 2nd recursive call.
    # * return_value - our return value.

    class StackFrame:
        def __init__(self, *, return_addr, n):
            self.return_addr = return_addr
            self.n = n
            self.r1 = None
            self.r2 = None
            self.return_value = None

    # Variables in function fibo:
    # * cs - our call stack.
    # * tmp - holds return value during pop of call stack.
    # * skip_to - location to "goto" after continue; possible values:
    #   * 0 - making recursive call; goto start of function.
    #   * 1 - returning from recursive call #1.
    #   * 2 - returning from recursive call #2.

    # Local variables from original function, along with return address
    # and return value, are stored in the top stack item (cs[-1):
    # * return_addr
    # * n
    # * r1
    # * r2
    # * return_value

    # **************************************************
    # SETUP CALL STACK
    # **************************************************

    cs = list()  # Call stack
    cs.append(StackFrame(return_addr=0, n=n))

    # **************************************************
    # BEGIN LOOP
    # while True loop used for recursion elimination
    # **************************************************

    skip_to = 0
    while True:

        if skip_to == 0:

            # BASE CASE

            # **************************************************
            # ORIGINAL CODE:
            # if n <= 1:
            #     return n
            # **************************************************

            assert len(cs) > 0
            if cs[-1].n <= 1:
                cs[-1].return_value = cs[-1].n

                if cs[-1].return_addr == 0:
                    tmp = cs[-1].return_value
                    cs.pop()
                    assert len(cs) == 0
                    return tmp
                skip_to = cs[-1].return_addr
                assert skip_to == 1 or skip_to == 2
                continue

            # RECURSIVE CASE

            # **************************************************
            # ORIGINAL CODE:
            # r1 = fibo(n-2)  # Recursive call #1
            # **************************************************

            assert len(cs) > 0
            cs.append(StackFrame(return_addr=1, n=cs[-1].n-2))
            skip_to = 0
            continue

        if skip_to == 0 or skip_to == 1:
            skip_to = 0

            # Return from recursive call #1 here

            assert len(cs) > 0
            tmp = cs[-1].return_value
            cs.pop()
            assert len(cs) > 0
            cs[-1].r1 = tmp

            # **************************************************
            # ORIGINAL CODE:
            # r2 = fibo(n-1)  # Recursive call #2
            # **************************************************

            assert len(cs) > 0
            cs.append(StackFrame(return_addr=2, n=cs[-1].n-1))
            skip_to = 0
            continue

        if skip_to == 0 or skip_to == 2:
            skip_to = 0

            # Return from recursive call #2 here

            assert len(cs) > 0
            tmp = cs[-1].return_value
            cs.pop()
            assert len(cs) > 0
            cs[-1].r2 = tmp

            # **************************************************
            # ORIGINAL CODE:
            # return r1 + r2  # Return the result
            # **************************************************

            cs[-1].return_value = cs[-1].r1 + cs[-1].r2

            if cs[-1].return_addr == 0:
                tmp_return_value = cs[-1].return_value
                cs.pop()
                assert len(cs) == 0
                return tmp_return_value
            skip_to = cs[-1].return_addr
            assert skip_to == 1 or skip_to == 2
            continue


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    print("", end="", flush=True)
    _ = input(msg)


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

