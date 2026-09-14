#!/usr/bin/env python3
# use_llist.py
# Glenn G. Chappell
# Started: 2026-09-13
# Updated: 2026-09-14
"""Singly Linked List example: create & find size.
For CS 311 Fall 2026
"""


import llnode  # For ._LLNode
import sys  # For .stdout


def size(head):
    """Return size of a Linked List, given its head.

    Pre:
    - head is None or llnode._LLNode.
    """

    assert (head is None) or isinstance(head, llnode._LLNode)

    p = head
    counter = 0
    while p is not None:
        p = p.next
        counter += 1

    return counter


def user_pause(msg):
    """Wait for user to press ENTER."""

    assert isinstance(msg, str)

    sys.stdout.flush()
    dummy = input(msg)


# Main program
# Create Linked List, add nodes, find size.

if __name__ == "__main__":

    THE_SIZE = 507  # Size of list to create

    # Create empty Linked List
    print("Creating empty Linked List")
    head = None

    # Add nodes to Linked List
    print()
    print(f"Adding {THE_SIZE} nodes to Linked List")
    for i in range(THE_SIZE):
        head = llnode._LLNode(THE_SIZE-i, head)

    # Find & print size of Linked List
    print()
    s = size(head)
    print(f"Computed size of Linked List: {s} - ", end="")
    if s == THE_SIZE:
        print("right!")
    else:
        print("WRONG *************************************************")

    print()
    user_pause("Press ENTER to quit ")

