# allocator.py
# Glenn G. Chappell
# 2026-10-13
"""Class Allocator: memory allocator for array.
For CS 311 Fall 2026
"""


class Allocator:
    """Memory allocator: holds array accessible via bracket op."""

    # Attributes:
    # * _data: list of specified size

    def __init__(self, size):
        """Allocate list of specified size."""

        assert isinstance(size, int)
        assert size >= 0

        self._data = [ None for _ in range(size) ]

    def __getitem__(self, ix):
        """Return item in array with given index.
        Return None on out-of-range index.
        """

        assert isinstance(ix, int)

        try:
            return self._data[ix]
        except:
            return None  # Fail silently

    def __setitem__(self, ix, val):
        """Set item in array with given index to given value.
        Does nothing on out-of-range index.
        """

        assert isinstance(ix, int)

        try:
            self._data[ix] = val
        except:
            pass         # Fail silently

# End class Allocator

