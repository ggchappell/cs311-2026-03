# heap_algs.py  UNFINISHED
# Glenn G. Chappell
# 2026-11-03
"""Heap Algorithms.
For CS 311 Fall 2026

All functions are given a range as container, index1, index2.
* container is an indexable sequence.
* index1, index2 are indices for container: first item in the range,
  just past the last item in the range. Negative indices are handled as
  usual in Python.
* In public functions, the indices may be omitted to indicate the whole
  container.

A *relative index* is an index relative to index1. For example, if i is
a relative index, then the actual index is index1+i, and we do
container[index1+i].

By a *Heap* we mean a Binary Heap in the usual array representation. The
root item is at relative index 0.
"""


def heap_test(container, index1=None, index2=None):
    """Return True if given range is a Heap."""

    if index1 is None:
        index1 = 0
    if index2 is None:
        index2 = len(container)
    assert isinstance(index1, int)
    assert isinstance(index2, int)
    if index1 < 0:
        index1 += len(container)
    if index2 < 0:
        index2 += len(container)
    assert 0 <= index1 <= index2 <= len(container)

    size = index2 - index1
    assert size >= 0

    for curr in range(1, size):
        # curr is relative index of item to compare with its parent
        parent = (curr-1) // 2  # Relative index of parent
        if container[index1+parent] < container[index1+curr]:
            return False
    return True


def heap_insert(container, index1=None, index2=None):
    """Insert last item in range into Heap of previous items."""

    # TODO: WRITE THIS!!!


def heap_delete(container, index1=None, index2=None):
    """Given Heap, delete first item, placing it at end of range."""

    # TODO: WRITE THIS!!!


def heap_make(container, index1=None, index2=None):
    """Given a range, make it into a Heap."""

    # TODO: WRITE THIS!!!


def heap_to_sorted(container, index1=None, index2=None):
    """Given a Heap, sort it by "<", ascending. Not stable."""

    # TODO: WRITE THIS!!!

