#!/usr/bin/env python3
# except.py
# Glenn G. Chappell
# 2026-09-04
"""Demonstrate Python exceptions.
For CS 311 Fall 2026
"""


def ff():
    """Do various exception-y stuff."""

    try:
        print("A")
        #raise IndexError("yo")
        #raise ValueError("yo")
        #return
        print("B")
    except IndexError as e:
        print("C")
    finally:
        print("D")


# Main program

if __name__ == "__main__":
    print("Try uncommenting some of the commented-out lines in this")
    print("program. Predict what the program will do. Then run it and")
    print("see if you were right.")
    print()

    print("X")
    ff()
    print("Y")

