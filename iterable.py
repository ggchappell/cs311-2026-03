#!/usr/bin/env python3
# iterable.py
# Glenn G. Chappell
# 2026-09-09
"""Example of iterable class and its use.
For CS 311 Fall 2026
"""


import sys  # For .stdout


class Squares:
    """Iterable. Gives 0^2, 1^2, ..., (n-1)^2. n is initializer arg."""

    # Attributes:
    # * _end: positive int; we compute squares of integers in integers [0, _end).

    def __init__(self, end=None):
        """Create iterable with given end value (default: 10)."""

        if end is None:
            end = 10
        assert isinstance(end, int)
        assert end > 0

        self._end = end

    def __iter__(self):
        """Return iterator for this object."""

        return _SquaresIterator(self)

# End class Squares


class _SquaresIterator:
    """Iterator for type Squares. Internal-use only."""
    # See class Squares, above.

    # Attributes:
    # * _the_sq: the Squares object we iterate through.
    # * _value: next value to square & return.

    def __init__(self, the_sq):
        """Create iterator for given Squares object."""

        assert isinstance(the_sq, Squares)

        self._the_sq = the_sq
        self._value = 0

    def __next__(self):
        """Return next square or raise StopIteration if end reached."""

        # Done?
        if self._value >= self._the_sq._end:
            raise StopIteration()

        # Compute & return next value
        save_val = (self._value)**2
        self._value += 1
        return save_val

    def __iter__(self):
        """An iterator is an iterable; return this object."""

        return self

# End class _SquaresIterator


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    sys.stdout.flush()
    dummy = input(msg)


# Main program
# Create and use a Squares iterable.

if __name__ == "__main__":
    print("Example iterable class: Squares")
    print()

    print("Doing for-in loop using Squares(7):")
    for i in Squares(7):
        print(i)

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

