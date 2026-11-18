# reverser.py
# Glenn G. Chappell
# 2026-11-18
"""Class for function objects that reverse items.
For CS 311 Fall 2026
"""


class Reverser:
    """Objects are callable; pass a range to reverse it.
    """

    def __call__(self, container, index1=None, index2=None):
        """Reverse the given range.
        Range to be reversed is [container[index1], container[index2]),
        or the whole container if index1, index2 are not passed.

        Pre:
        * container is an indexable sequence.
        * If index1, index2 are both given, then:
          * index1 and index2 have type int.
          * index1 <= index2.
          * Integers in [index1, index2) are valid indices for
            container.
        """

        if index1 is None:
            index1 = 0
        assert isinstance(index1, int)
        if index2 is None:
            index2 = len(container)
        assert isinstance(index2, int)
        assert index2 >= index1

        size = index2 - index1
        for i in range(size):
            ix1 = index1 + i
            ix2 = index2-i-1
            if ix2 <= ix1:
                break
            container[ix1], container[ix2] = (  # Swap
                container[ix2], container[ix1])

# End class Reverser

