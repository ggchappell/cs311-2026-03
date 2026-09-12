#!/usr/bin/env python3
# indexable.py
# Glenn G. Chappell
# 2026-09-11
"""Example of indexable class and its use.
For CS 311 Fall 2026
"""


import sys  # For .stdout


class Cubes:
    """Indexable. obj[i] is i^3 if i in [0..n). n is initializer arg."""

    def __init__(self, end=None):
        """Create indexable for indices in [0, end) (default: 10)."""

        if end is None:
            end = 10
        assert isinstance(end, int)

        self._end = end

    def __getitem__(self, ix):
        """Return value for given index."""

        assert isinstance(ix, int)
        if not (0 <= ix < self._end):
            raise IndexError("Cubes.__getitem__: bad index")

        return ix * ix * ix


def user_pause(msg):
    """Wait for user to press ENTER."""

    assert isinstance(msg, str)

    sys.stdout.flush()
    dummy = input(msg)


# Main program
# Create Cubes object and use it.

if __name__ == "__main__":
    print("Example indexable class: Cubes")

    print()
    print("Create Cubes(7) object x and print x[2].")
    x = Cubes(7)
    print(f"  x[2] = {x[2]}")

    print()
    print("Iterate through x (an indexable is magically an iterable).")
    print("Use enumerate.")
    for ix, val in enumerate(x):
        print(f"  {ix}: {val}")

    print()
    user_pause("Press ENTER to quit ")

