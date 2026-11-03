#!/usr/bin/env python3
# heap_algs_main.cpp
# Glenn G. Chappell
# 2026-11-03
"""Simple main program for Heap algorithms.
For CS 311 Fall 2026
"""


import heap_algs  # For .heap_test, .heap_insert, .heap_delete,
                  # .heap_make, .heap_to_sorted


def is_sorted(container):
    for i in range(len(container)-1):
        if container[i+1] < container[i]:
            return False
    return True


def print_info(container, expect_heap):
    print(container)

    is_heap = heap_algs.heap_test(container)

    print(f"The above is{'' if is_heap else ' NOT'} a heap ", end="")
    if expect_heap == is_heap:
        print("(good)")
    else:
        print("(BAD " + "*"*40 + ")")


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    print("", end="", flush=True)
    _ = input(msg)


# Main program
# Demonstrates use of Heap algorithms.

if __name__ == "__main__":

    # ***** First Dataset *****

    print("-"*40)
    print()

    # Initialize dataset #1
    print("Initialize dataset #1")
    print()
    d1 = [20, 12, 8, 5, 10, 8, 4, 3, 1, 2]

    print_info(d1, True)
    print()

    # Do an insert
    val = 15
    print(f"Heap insert {val}")
    print()
    d1.append(val)
    heap_algs.heap_insert(d1)

    print_info(d1, True)
    print()

    # Do another insert
    val = 11
    print(f"Heap insert {val}")
    print()
    d1.append(val)
    heap_algs.heap_insert(d1)

    print_info(d1, True)
    print()

    # ***** Second Dataset *****

    print("-"*40)
    print()

    # Initialize dataset #2
    print("Initialize dataset #2")
    print()
    d2 = [5, 3, 2, 9, 6, 7, 10, 4, 5, 1, -4]

    print_info(d2, False)
    print()

    # Make a heap
    print("Heap make")
    print()
    heap_algs.heap_make(d2)

    print_info(d2, True)
    print()

    # Do an insert
    val = 8
    print(f"Heap insert {val}")
    print()
    d2.append(val)
    heap_algs.heap_insert(d2)

    print_info(d2, True)
    print()

    # Do a delete
    print("Heap delete")
    print()
    heap_algs.heap_delete(d2)
    d2.pop()

    print_info(d2, True)
    print()

    # Sort it
    print("Heap -> sorted")
    print()
    heap_algs.heap_to_sorted(d2)

    print_info(d2, False)
    if is_sorted(d2):
        print("The above is sorted (good)")
    else:
        print("The above is NOT sorted (BAD " + "*"*40 + ")")
    print()

    # ***** Done *****

    print("-"*40)

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

