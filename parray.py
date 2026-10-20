# parray.py  HAND-OFF
# Glenn G. Chappell
# Started: 2026-10-14
# Updated: 2026-10-19
"""Class PArray: array data structure.
"""


import allocator  # For .Allocator


# Minimum capacity for a PArray object
_MIN_CAPACITY = 8


class PArray:
    """Array data structure. Similar to list."""

    # Attributes:
    # * _alloc: allocator. Callable. Takes size, returns data object.
    # * _data: data object. Holds array of _size items.
    # * _size: size of our array.
    #
    # Class invariants:
    # * _alloc is the allocator passed to __init__, or
    #   allocator.Allocator, if this was omitted.
    # * _data is a data object returned by _alloc, which can hold at
    #   least _size items.
    # * _size >= 0.

    def __init__(self, iterable=None, *, alloc=None):
        """Initialize from optional iterator. Use optional allocator."""

        if alloc is None:
            alloc = allocator.Allocator
        assert callable(alloc)
        self._alloc = alloc

        if iterable is None:
            iterable = []

        dataset = list(iterable)
        self._size = len(dataset)
        self._data = self._alloc(self._size)
        for i in range(self._size):
            self._data[i] = dataset[i]

    def __getitem__(self, ix):
        """Return item with given index."""

        assert isinstance(ix, int)
        if ix < 0:
            ix += self._size

        if ix < 0 or ix >= self._size:
            raise IndexError("PArray.__getitem__: index out of range")
        return self._data[ix]

    def __setitem__(self, ix, value):
        """Set item with given index to given value."""

        assert isinstance(ix, int)
        if ix < 0:
            ix += self._size

        if ix < 0 or ix >= self._size:
            raise IndexError("PArray.__setitem__: index out of range")
        self._data[ix] = value

    def __delitem__(self, ix):
        """Delete item with given index."""

        _ = self.pop(ix)

    def __len__(self):
        """Return size of array."""

        return self._size

    def __bool__(self):
        """Return True if array is nonempty, else False."""
        return self._size != 0

    def __add__(self, iterable):
        """Return concatenation of self with given iterable."""

        cpy = self.copy()
        cpy.extend(iterable)
        return cpy

    def __iadd__(self, iterable):
        """Append values from iterable to self."""

        self.extend(iterable)
        return self

    def __str__(self):
        """String conversion, same as list."""

        result = "["
        for i in range(self._size):
            if i > 0:
                result += ", "
            result += repr(self._data[i])
        result += "]"
        return result

    def __repr__(self):
        """String conversion, like list with PArray(...) around it."""

        return "PArray(" + str(self) + ")"

    def copy(self):
        pass  # DUMMY
        # TODO: WRITE THIS!!!

    def sort(self, *, reverse=None, key=None):
        """Sort, rearranging items in array."""

        if reverse == None:
            reverse = False
        sorted_data = sorted(self, reverse=reverse, key=key)
        for i in range(self._size):
            self._data[i] = sorted_data[i]

    def resize(self, new_size):
        pass  # DUMMY
        # TODO: WRITE THIS!!!

    def insert(self, ix, val):
        pass  # DUMMY
        # TODO: WRITE THIS!!!

    def pop(self, ix=None):
        pass  # DUMMY
        # TODO: WRITE THIS!!!

    def append(self, value):
        """Append given value to array."""

        resize(self._size + 1)
        self._data[self._size-1] = value

    def extend(self, iterable):
        pass  # DUMMY
        # TODO: WRITE THIS!!!

    def index(self, value, start=None, stop=None):
        """Return index where value appears, or raise ValueError."""

        # Set a, b: our start, stop values
        if stop is None:
            a = 0
            b = self._size if start is None else start
        else:
            a = 0 if start is None else start
            b = stop

        # Make sure a,b have the right types
        assert isinstance(a, int)
        assert isinstance(b, int)

        # Handle negative indices as usual
        if a < 0:
            a += self._size
        if b < 0:
            b += self._size

        # If a,b are not within range, make them so
        a = max(a, 0)
        b = min(b, self._size)

        # Find our index
        for i in range(a, b):
            if self._data[i] == value:
                return i

        # Not found; raise exception
        raise ValueError("PArray.index: value not found")

# End class PArray

