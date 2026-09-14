# llnode.py
# Glenn G. Chappell
# 2026-09-13
"""Class _LLNode: Linked List node.
For CS 311 Fall 2026
"""

# **********************************************************************
# Class _LLNode - Class definition
# **********************************************************************


class _LLNode:
    """Linked List Node.

    Invariants:
    - next is either None or an _LLNode forming the head of a Linked
      List (with no cycles).
    """

    # ***** _LLNode: List of attributes *****

    # - data: this node's data item
    # - next: this node's next-node reference: None or _LLNode

    # ***** _LLNode: Initializer *****

    def __init__(self, data, next=None):
        """Set attributes to those given; next set to None if not given.

        Pre:
        - next is None or _LLNode forming the head of a Linked List
          (with no cycles).
        """

        self.data = data
        self.next = next  # No need to check for None!

# End class _LLNode

