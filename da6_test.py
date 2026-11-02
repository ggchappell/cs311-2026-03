#!/usr/bin/env python3
# da6_test.py
# Glenn G. Chappell
# 2026-11-01
"""Test program for Assignment 6 functions & classes.
For CS 311 Fall 2026

For Assignment 3, Exercises A-B
Requires da6.py, llnode.py
"""

# Import for code to be tested
import da6        # For .reverse_list, .LLDict

# Import for testing framework
import unittest   # For .TestCase, .main

# Other imports for test suite
import llnode     # For ._LLNode
import copy       # For .copy


# **********************************************************************
# Test Cases
# **********************************************************************


# ***** Tests for Function reverse_list *****


class Test00ReverseListSizeItems(unittest.TestCase):
    def test00_empty(self):
        values = []
        head = make_ll(values)
        head = da6.reverse_list(head)
        llist_values = list(ll_iter(head))
        expected = list(reversed(values))

        self.assertEqual(llist_values, expected)

    def test01_size_1(self):
        values = [5]
        head = make_ll(values)
        head = da6.reverse_list(head)
        llist_values = list(ll_iter(head))
        expected = list(reversed(values))

        self.assertEqual(llist_values, expected)

    def test02_size_2(self):
        values = [14, "x"]
        head = make_ll(values)
        head = da6.reverse_list(head)
        llist_values = list(ll_iter(head))
        expected = list(reversed(values))

        self.assertEqual(llist_values, expected)

    def test03_size_3(self):
        values = [-3, "abc", 10.2]
        head = make_ll(values)
        head = da6.reverse_list(head)
        llist_values = list(ll_iter(head))
        expected = list(reversed(values))

        self.assertEqual(llist_values, expected)

    def test04_size_4(self):
        values = [True, -10, None, "z"]
        head = make_ll(values)
        head = da6.reverse_list(head)
        llist_values = list(ll_iter(head))
        expected = list(reversed(values))

        self.assertEqual(llist_values, expected)

    def test05_size_large(self):
        bignum = 100_000
        values = list(range(bignum))
        head = make_ll(values)
        head = da6.reverse_list(head)
        llist_values = list(ll_iter(head))
        expected = list(reversed(values))

        self.assertEqual(llist_values, expected)


class Test01ReverseListOther(unittest.TestCase):

    def test00_no_item_ops(self):
        values = [CreateCounter()] * 100
        head = make_ll(values)
        global create_count
        save_create_count = create_count
        head = da6.reverse_list(head)

        self.assertEqual(save_create_count, create_count)


# ***** Tests for Class LLDict *****


class Test02LLDictIter(unittest.TestCase):

    def test00_empty(self):
        expected = {}
        d = da6.LLDict()
        for k in expected:
            d[k] = expected[k]
        lldict_values = { k:v for k, v in d }

        self.assertEqual(lldict_values, expected)

    def test01_size_1(self):
        expected = {1:2}
        d = da6.LLDict()
        for k in expected:
            d[k] = expected[k]
        lldict_values = { k:v for k, v in d }

        self.assertEqual(lldict_values, expected)

    def test02_size_1_unhashable_key(self):
        expected = [([1,2],[3,4])]  # A list cannot be a dict key
        d = da6.LLDict()
        for k, v in expected:
            d[k] = v
        lldict_values_list = list(d)

        self.assertEqual(lldict_values_list, expected)

    def test03_size_2(self):
        expected = {3:"a",True:5.1}
        d = da6.LLDict()
        for k in expected:
            d[k] = expected[k]
        lldict_values = { k:v for k, v in d }

        self.assertEqual(lldict_values, expected)

    def test04_size_3(self):
        expected = {3:"a","a":[6,7],True:5.1}
        d = da6.LLDict()
        for k in expected:
            d[k] = expected[k]
        lldict_values = { k:v for k, v in d }

        self.assertEqual(lldict_values, expected)

    def test05_large(self):
        bignum = 5_000
        expected = { i:i*2 for i in range(bignum) }
        d = da6.LLDict()
        for k in expected:
            d[k] = expected[k]
        lldict_values = { k:v for k, v in d }

        self.assertEqual(lldict_values, expected)


class Test03LLDictGetitemLenDel(unittest.TestCase):

    def test00_empty(self):
        d = da6.LLDict()

        self.assertEqual(bool(d), False)
        self.assertEqual(len(d), 0)
        self.assertEqual(1 in d, False)
        self.assertEqual("x" in d, False)
        with self.assertRaises(KeyError):
            _ = d[1]
        with self.assertRaises(KeyError):
            del d["x"]
        self.assertEqual(len(d), 0)
        with self.assertRaises(KeyError):
            del d[1]
        self.assertEqual(bool(d), False)
        self.assertEqual(len(d), 0)
        self.assertEqual(1 in d, False)
        self.assertEqual("x" in d, False)
        with self.assertRaises(KeyError):
            _ = d[1]
        with self.assertRaises(KeyError):
            _ = d["x"]

    def test01_size_1(self):
        d = da6.LLDict()
        d[1] = "abc"

        self.assertEqual(bool(d), True)
        self.assertEqual(len(d), 1)
        self.assertEqual(1 in d, True)
        self.assertEqual("x" in d, False)
        self.assertEqual(d[1], "abc")
        with self.assertRaises(KeyError):
            _ = d["x"]
        with self.assertRaises(KeyError):
            del d["x"]
        self.assertEqual(len(d), 1)
        del d[1]
        self.assertEqual(bool(d), False)
        self.assertEqual(len(d), 0)
        self.assertEqual(1 in d, False)
        self.assertEqual("x" in d, False)
        with self.assertRaises(KeyError):
            _ = d[1]
        with self.assertRaises(KeyError):
            _ = d["x"]

    def test02_size_2(self):
        d = da6.LLDict()
        d[1] = "abc"
        d["x"] = True

        self.assertEqual(bool(d), True)
        self.assertEqual(len(d), 2)
        self.assertEqual(1 in d, True)
        self.assertEqual("x" in d, True)
        self.assertEqual(d[1], "abc")
        self.assertEqual(d["x"], True)
        del d["x"]
        self.assertEqual(len(d), 1)
        del d[1]
        self.assertEqual(bool(d), False)
        self.assertEqual(len(d), 0)
        self.assertEqual(1 in d, False)
        self.assertEqual("x" in d, False)
        with self.assertRaises(KeyError):
            _ = d[1]
        with self.assertRaises(KeyError):
            _ = d["x"]

    def test03_size_3(self):
        d = da6.LLDict()
        d[1] = "abc"
        d["x"] = True
        d[False] = 7

        self.assertEqual(bool(d), True)
        self.assertEqual(len(d), 3)
        self.assertEqual(1 in d, True)
        self.assertEqual("x" in d, True)
        self.assertEqual(d[1], "abc")
        self.assertEqual(d["x"], True)
        del d["x"]
        self.assertEqual(len(d), 2)
        del d[1]
        self.assertEqual(bool(d), True)
        self.assertEqual(len(d), 1)
        self.assertEqual(1 in d, False)
        self.assertEqual("x" in d, False)
        with self.assertRaises(KeyError):
            _ = d[1]
        with self.assertRaises(KeyError):
            _ = d["x"]

    def test04_large(self):
        bignum = 1_000
        half = bignum//2
        d = da6.LLDict()
        for i in range(bignum):
            d[i] = i*i
            d[str(i)] = i

        self.assertEqual(bool(d), True)
        self.assertEqual(len(d), 2*bignum)
        self.assertEqual(2 in d, True)
        self.assertEqual("2" in d, True)
        self.assertEqual(half in d, True)
        self.assertEqual(str(half) in d, True)
        self.assertEqual(d[2], 2*2)
        self.assertEqual(d["2"], 2)
        self.assertEqual(d[half], half*half)
        self.assertEqual(d[str(half)], half)

        del d[half]

        self.assertEqual(len(d), 2*bignum-1)
        self.assertEqual(2 in d, True)
        self.assertEqual("2" in d, True)
        self.assertEqual(half in d, False)
        self.assertEqual(str(half) in d, True)
        self.assertEqual(d[2], 2*2)
        self.assertEqual(d["2"], 2)
        with self.assertRaises(KeyError):
            _ = d[half]
        self.assertEqual(d[str(half)], half)

        del d[str(half)]

        self.assertEqual(len(d), 2*bignum-2)
        self.assertEqual(2 in d, True)
        self.assertEqual("2" in d, True)
        self.assertEqual(half in d, False)
        self.assertEqual(str(half) in d, False)
        self.assertEqual(d[2], 2*2)
        self.assertEqual(d["2"], 2)
        with self.assertRaises(KeyError):
            _ = d[half]
        with self.assertRaises(KeyError):
            _ = d[str(half)]

        d[half] = True

        self.assertEqual(len(d), 2*bignum-1)
        self.assertEqual(2 in d, True)
        self.assertEqual("2" in d, True)
        self.assertEqual(half in d, True)
        self.assertEqual(str(half) in d, False)
        self.assertEqual(d[2], 2*2)
        self.assertEqual(d["2"], 2)
        self.assertEqual(d[half], True)
        with self.assertRaises(KeyError):
            _ = d[str(half)]

        d[str(half)] = False

        self.assertEqual(len(d), 2*bignum)
        self.assertEqual(2 in d, True)
        self.assertEqual("2" in d, True)
        self.assertEqual(half in d, True)
        self.assertEqual(str(half) in d, True)
        self.assertEqual(d[2], 2*2)
        self.assertEqual(d["2"], 2)
        self.assertEqual(d[half], True)
        self.assertEqual(d[str(half)], False)


class Test04LLDictModify(unittest.TestCase):

    def test00_small_a(self):
        d = da6.LLDict()
        d[1] = "one"
        d["two"] = 2
        d[3.5] = 4.5
        d[False] = True
        del d[3.5]
        d[1] = 7
        d[3.5] = 1
        del d[False]
        lldict_values = { k:v for k, v in d }
        expected = { 1:7, "two":2, 3.5:1 }

        self.assertEqual(lldict_values, expected)

    def test01_small_b(self):
        d = da6.LLDict()
        d[3] = 4
        d[1] = 2
        d[2] = 3
        d[4] = 5
        del d[1]
        d[3] = 5
        d[2] = 4
        d[0] = 2
        lldict_values = { k:v for k, v in d }
        expected = { 0:2, 2:4, 3:5, 4:5 }

        self.assertEqual(lldict_values, expected)

    def test02_large(self):
        bignum = 1_000
        d = da6.LLDict()
        for i in range(3*bignum):
            d[i] = i+1
        for i in range(bignum, 4*bignum):
            d[i] = i+2
        for i in range(2*bignum, 3*bignum):
            del d[i]
        lldict_values = { k:v for k, v in d }
        expected = ( { i:i+1 for i in range(bignum) }
                   | { i:i+2 for i in range(bignum, 2*bignum) }
                   | { i:i+2 for i in range(3*bignum, 4*bignum) } )

        self.assertEqual(lldict_values, expected)


class Test04LLDictCopy(unittest.TestCase):

    def test00_noncopy(self):
        d = da6.LLDict()
        d2 = da6.LLDict()
        d[1] = 1
        d2[1] = 2
        lldict_values = { k:v for k, v in d }
        expected = { 1:1 }
        lldict2_values = { k:v for k,v in d2 }
        expected2 = { 1:2 }

        self.assertEqual(lldict_values, expected)
        self.assertEqual(lldict2_values, expected2)

    def test01_copy_a(self):
        d = da6.LLDict()
        d2 = copy.copy(d)
        lldict_values = { k:v for k, v in d }
        expected = {}
        lldict2_values = { k:v for k,v in d2 }
        expected2 = {}

        self.assertEqual(lldict_values, expected)
        self.assertEqual(lldict2_values, expected2)

        d[1] = 1
        d2[1] = 2
        lldict_values = { k:v for k, v in d }
        expected = { 1:1 }
        lldict2_values = { k:v for k,v in d2 }
        expected2 = { 1:2 }

        self.assertEqual(lldict_values, expected)
        self.assertEqual(lldict2_values, expected2)

    def test02_copy_b(self):
        d = da6.LLDict()
        d[1] = 10
        d2 = copy.copy(d)
        d2[1] = 11
        lldict_values = { k:v for k, v in d }
        expected = { 1:10 }
        lldict2_values = { k:v for k,v in d2 }
        expected2 = { 1:11 }

        self.assertEqual(lldict_values, expected)
        self.assertEqual(lldict2_values, expected2)

    def test03_copy_c(self):
        d = da6.LLDict()
        d[1] = 2
        d[4] = 5
        d[2] = 3
        d[3] = 4
        del d[2]
        d[3] = 5
        d2 = copy.copy(d)
        d2[2] = 4
        del d2[1]
        d2[3] = 6
        d[10] = 12
        lldict_values = { k:v for k, v in d }
        expected = { 1:2, 3:5, 4:5, 10:12 }
        lldict2_values = { k:v for k,v in d2 }
        expected2 = { 2:4, 3:6, 4:5 }

        self.assertEqual(lldict_values, expected)
        self.assertEqual(lldict2_values, expected2)

    def test04_copy_same_order(self):
        bignum = 1_000
        d = da6.LLDict()
        for i in range(0, 2*bignum, 2):
            d[i] = 1
        for i in range(2*bignum-1, -1, -2):
            d[i] = 1
        d2 = copy.copy(d)
        lldict_values_list = list(d)
        lldict2_values_list = list(d2)
        expected_sorted = [ (i,1) for i in range(2*bignum) ]

        self.assertEqual(sorted(lldict_values_list), expected_sorted)
        self.assertEqual(lldict_values_list, lldict2_values_list)


# **********************************************************************
# Helper Code
# **********************************************************************


def make_ll(the_list):
    import llnode

    head = None
    for value in reversed(the_list):
        head = llnode._LLNode(value, head)
    return head


def ll_size(head):
    """Return size of an _LLNode Linked List, given its head.

    Pre:
    * head is None or llnode._LLNode.
    """

    assert (head is None) or isinstance(head, llnode._LLNode)

    p = head
    counter = 0
    while p is not None:
        p = p.next
        counter += 1

    return counter


class _LLIter:
    """Helper class for function ll_iter."""

    def __init__(self, the_linked_list):
        self._p = the_linked_list

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self._p is None:
                raise StopIteration()
            elif isinstance(self._p, llnode._LLNode):
                val = self._p.data
                self._p = self._p.next
                return val
            else:
                raise ValueError("Improperly formatted Linked List")


def ll_iter(the_linked_list):
    """Return an iterator for an _LLNode Linked List, given its head.

    Pre:
    * head is None or llnode._LLNode.
    """

    return _LLIter(the_linked_list)


# Number of calls to CreateCounter.__init__
create_count = 0


class CreateCounter:
    """Class that increments global create_count on __init__."""

    def __init__(self):
        global create_count
        create_count += 1



# **********************************************************************
# Main Program
# **********************************************************************


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    print("", end="", flush=True)
    _ = input(msg)


# Main program

if __name__ == '__main__':
    # Printable name for this test suite
    test_suite_name = ("Assignment 6 Functions & Classes"
                     + "- CS 311 Assn 3, Exs A-B")

    # Run tests & print results
    print(f"BEGIN tests for {test_suite_name}")
    unittest.main(exit=False)  # This call will return
    print(f"END tests for {test_suite_name}")

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

