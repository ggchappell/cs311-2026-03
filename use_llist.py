#!/usr/bin/env python3
# use_llist.py
# Glenn G. Chappell
# Started: 2026-09-13
# Updated: 2026-10-23
"""Singly Linked List example: create & find size.
For CS 311 Fall 2026
"""


import llnode  # For ._LLNode


def size(head):
    """Return size of a Linked List, given its head.

    Pre:
    * head is None or llnode._LLNode.
    """

    assert (head is None) or isinstance(head, llnode._LLNode)

    p = head
    counter = 0
    while p is not None:
        p = p.next
        counter += 1

    return counter


def copy(head):
    """Return a shallow copy of a Linked List, given its head.

    Pre:
    * head is None or llnode._LLnode.
    """

    assert (head is None) or isinstance(head, llnode._LLNode)

    if head is None:
        return None

    new_head = llnode._LLNode(head.data)
    last = new_head
    p = head.next

    while p is not None:
        last.next = llnode._LLNode(p.data)
        last = last.next
        p = p.next

    return new_head


def mult_all(head, i):
    """Replace each item in Linked List by i * the item.

    Pre:
    * head is None or llnode._LLnode.
    * i is an int.
    """

    assert (head is None) or isinstance(head, llnode._LLNode)
    assert isinstance(i, int)

    p = head
    while p is not None:
        p.data *= i
        p = p.next


def print_llist(head):
    """Print blank-separated Linked List items, then blank, newline.

    Pre:
    * head is None or llnode._LLnode.
    """

    assert (head is None) or isinstance(head, llnode._LLNode)

    p = head
    while p is not None:
        print(str(p.data) + " ", end="")
        p = p.next
    print()


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    print("", end="", flush=True)
    _ = input(msg)


# Main program
# Create Linked List, add nodes, find size.

if __name__ == "__main__":

    THE_SIZE = 18  # Size of list to create

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

    # Make a copy, modify it, print both
    print()
    i = 10
    print(f"Making a copy and multiplying by {i}.")
    new_head = copy(head)
    mult_all(new_head, i)
    print("Original: ", end="")
    print_llist(head)
    print("Modified copy: ", end="")
    print_llist(new_head)

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

