# heap_algs.py
# Glenn G. Chappell
# Started: 2026-11-03
# Updated: 2026-11-04
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
    assert 0 <= index1 < index2 <= len(container)

    size = index2 - index1
    assert size >= 1

    curr = size-1     # Relative index of item to sift up
    while curr != 0:  # While current item is not the root
        parent = (curr-1) // 2  # Relative index of parent
        if not (container[index1+parent] < container[index1+curr]):
            break  # No more sifting; done

        # Sift up one level
        container[index1+curr], container[index1+parent] = (  # Swap
            container[index1+parent], container[index1+curr])
        curr = parent


def _sift_down(container, index1, index2, location):
    """Sift down of item at given location into existing partial Heap.
    Internal-use function for heap_delete, heap_make.
    location is absolute (not relative) index of item to sift down.
    """

    assert isinstance(index1, int)
    assert isinstance(index2, int)
    assert isinstance(location, int)
    if index1 < 0:
        index1 += len(container)
    if index2 < 0:
        index2 += len(container)
    if location < 0:
        location += len(container)
    assert 0 <= index1 <= location < index2 <= len(container)

    size = index2 - index1
    assert size >= 1

    curr = location - index1  # Relative index of item to sift down.
    while True:
        lchild = 2*curr+1   # Relative index of left child, if any
        if lchild >= size:  # Are there any children?
            break           # If not, done

        bigchild = lchild   # Relative index of bigger child
        if (lchild+1 < size
          and container[index1+lchild] < container[index1+lchild+1]):
            bigchild = lchild+1  # Bigger child is right child

        if not (container[index1+curr] < container[index1+bigchild]):
            break  # No more sifting; done

        # Sift down one level
        container[index1+curr], container[index1+bigchild] = (  # Swap
            container[index1+bigchild], container[index1+curr])
        curr = bigchild


def heap_delete(container, index1=None, index2=None):
    """Given Heap, delete first item, placing it at end of range."""

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
    assert 0 <= index1 < index2 <= len(container)

    size = index2 - index1
    assert size >= 1

    # Nothing to do if Heap has size 1
    if size < 2:
        return

    container[index1], container[index2-1] = (  # Swap
        container[index2-1], container[index1])
    _sift_down(container, index1, index2-1, index1)


def heap_make(container, index1=None, index2=None):
    """Given a range, make it into a Heap."""

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

    for curr in range((size-2) // 2, -1, -1):
        _sift_down(container, index1, index2, index1+curr)

    # Above is the linear-time method. Below is the more obvious
    # method, which WORKS, but requires log-linear time.
    #
    # for curr_size in range(2, size):
    #     heap_insert(container, index1, index1+curr_size)


def heap_to_sorted(container, index1=None, index2=None):
    """Given a Heap, sort it by "<", ascending. Not stable."""

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

    for curr_size in range(size, 1, -1):
        heap_delete(container, index1, index1+curr_size)

