# parray.py  UNFINISHED
# Glenn G. Chappell
# 2026-10-14
"""Class PArray: array data structure.
"""


import allocator  # For .Allocator


class PArray:
    def __init__(self, iterable=None, *, alloc=None):
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
        if ix < 0 or ix >= self._size:
            raise IndexError("PArray: index out of range")
        return self._data[ix]

    def __setitem__(self, ix, val):
        if ix < 0 or ix >= self._size:
            raise IndexError("PArray: index out of range")
        self._data[ix] = val

    def __delitem__(self, ix):
        pass

    def __len__(self):
        pass

    def __bool__(self):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __str__(self):
        result = "["
        for i in range(self._size):
            if i > 0:
                result += ", "
            result += repr(self._data[i])
        result += "]"
        return result

    def __repr__(self):
        return "PArray(" + str(self) + ")"

    def copy(self):
        pass

    def sort(self, *, reverse=None, key=None):
        pass

    def resize(self, new_size):
        pass

    def insert(self, ix, val):
        pass

    def pop(self, ix=None):
        pass

    def append(self, val):
        pass

    def extend(self, iterable):
        pass

    def index(self, val, start=None, end=None):
        pass

# End class PArray

