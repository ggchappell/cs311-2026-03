#!/usr/bin/env python3
# da3_test.py
# Glenn G. Chappell
# 2026-09-22
"""Test program for Assignment 3 functions.
For CS 311 Fall 2026

For Assignment 3, Exercises A-D
Requires da3.py
"""

# Import for code to be tested
import da3     # For .ll_iter, .create_ll, .does_it_raise, .mcss

# Import for testing framework
import unittest   # For .TestCase, .main

# Other imports for test suite
import sys        # For .stdout
import itertools  # For .islice


# **********************************************************************
# Test Cases
# **********************************************************************


class TestLLIter(unittest.TestCase):

    def test_empty(self):
        the_list = []
        the_ll = make_ll(the_list)
        result = list(da3.ll_iter(the_ll))

        self.assertEqual(result, the_list)

    def test_small_list(self):
        the_list = [2, 18, 7]
        the_ll = make_ll(the_list)
        result = list(da3.ll_iter(the_ll))

        self.assertEqual(result, the_list)

    def test_small_list_details(self):
        the_list = [1, 5, 4]
        the_iterable = da3.ll_iter(make_ll(the_list))
        the_iter = iter(the_iterable)

        v = next(the_iter)
        self.assertEqual(v, the_list[0])
        v = next(the_iter)
        self.assertEqual(v, the_list[1])
        v = next(the_iter)
        self.assertEqual(v, the_list[2])
        with self.assertRaises(StopIteration):
            v = next(the_iter)

    def test_big_list(self):
        big_num = 1_000_000
        the_list = [9] + [5]*big_num + [2] + [4]*big_num + [7]
        the_ll = make_ll(the_list)
        result = list(da3.ll_iter(the_ll))

        self.assertEqual(result, the_list)

    def test_cycle_list(self):
        import llnode

        the_list = [7, 2]
        dups = 50
        the_ll = make_ll(the_list)
        the_ll.next.next = the_ll  # Cheating: Linked List w/ cycle
        result = list(itertools.islice(da3.ll_iter(the_ll), dups*2))

        self.assertEqual(result, the_list*dups)

    def test_raise1(self):
        the_bad_ll = 5

        with self.assertRaises(ValueError):
            result = list(da3.ll_iter(the_bad_ll))

    def test_raise2(self):
        import llnode

        the_bad_ll = llnode._LLNode(1, 2)

        with self.assertRaises(ValueError):
            result = list(da3.ll_iter(the_bad_ll))


class TestCreateLL(unittest.TestCase):

    def test_empty(self):
        import llnode

        the_list = []
        created_llist = da3.create_ll(the_list)

        # Check that constructed Linked List has the right values
        p = created_llist
        for v in the_list:
            self.assertIsInstance(p, llnode._LLNode)
            self.assertEqual(p.data, v)
            p = p.next
        self.assertIs(p, None)

    def test_small_list(self):
        import llnode

        the_list = [2, 8, 5]
        created_llist = da3.create_ll(the_list)

        # Check that constructed Linked List has the right values
        p = created_llist
        for v in the_list:
            self.assertIsInstance(p, llnode._LLNode)
            self.assertEqual(p.data, v)
            p = p.next
        self.assertIs(p, None)

    def test_small_iterable(self):
        import llnode

        the_list = [2, 8, 5]
        the_iterable = itertools.islice(the_list, None)
        created_llist = da3.create_ll(the_iterable)

        # Check that constructed Linked List has the right values
        p = created_llist
        for v in the_list:
            self.assertIsInstance(p, llnode._LLNode)
            self.assertEqual(p.data, v)
            p = p.next
        self.assertIs(p, None)

    def test_big_list(self):
        import llnode

        big_num = 1_000_000
        the_list = [1] + [8]*big_num + [2] + [7]*big_num + [3]
        created_llist = da3.create_ll(the_list)

        # Check that constructed Linked List has the right values
        p = created_llist
        for v in the_list:
            self.assertIsInstance(p, llnode._LLNode)
            self.assertEqual(p.data, v)
            p = p.next
        self.assertIs(p, None)


class TestDidItRaise(unittest.TestCase):

    def test_not_callable(self):
        bad_func = 42

        with self.assertRaises(TypeError):
            result = da3.did_it_raise(bad_func)

    def test_no_raise_no_return(self):
        def ff():
            pass

        result = da3.did_it_raise(ff)

        self.assertFalse(result)

    def test_no_raise_return(self):
        def ff():
            return 42

        result = da3.did_it_raise(ff)

        self.assertFalse(result)

    def test_raise_TypeError(self):
        def ff():
            raise(TypeError("Got some type probs, boss"))

        result = da3.did_it_raise(ff)

        self.assertTrue(result)

    def test_raise_IOError(self):
        def ff():
            raise(IOErro("Got some I/O probs, boss"))

        result = da3.did_it_raise(ff)

        self.assertTrue(result)


class TestMCSS(unittest.TestCase):

    def test_empty(self):
        the_list = []
        result = da3.mcss(the_list)
        expected = (0, 0, 0, 0)

        self.assertEqual(result, expected)

    def test_size_1_pos(self):
        the_list = [3]
        result = da3.mcss(the_list)
        expected = (3, 3, 3, 3)

        self.assertEqual(result, expected)

    def test_size_1_neg(self):
        the_list = [-4]
        result = da3.mcss(the_list)
        expected = (0, 0, 0, -4)

        self.assertEqual(result, expected)

    def test_example_1(self):
        # First example from Assn 3 description
        the_list = [2, -3, 5, -4, 6, -10, 1]
        result = da3.mcss(the_list)
        expected = (7, 6, 1, -3)

        self.assertEqual(result, expected)

    def test_example_2(self):
        # Second example from Assn 3 description
        the_list = [-1, -2, -3]
        result = da3.mcss(the_list)
        expected = (0, 0, 0, -6)

        self.assertEqual(result, expected)

    def test_other_indexable(self):
        the_list = [2, -3, 5, -4, 6, -10, 1]
        the_indexable = tuple(the_list)
        result = da3.mcss(the_indexable)
        expected = (7, 6, 1, -3)

        self.assertEqual(result, expected)

    def test_long(self):
        big_num = 1_000_000
        the_list = ([1]*big_num + [-20_000_000] + [2]*big_num
                  + [-500_000] + [3]*big_num)
        result = da3.mcss(the_list)
        expected = (4_500_000, 1_000_000, 4_500_000, -14_500_000)

        self.assertEqual(result, expected)


# **********************************************************************
# Helper Code
# **********************************************************************


def make_ll(the_list):
    import llnode

    def make_node(d, n):
        return llnode._LLNode(d, n)

    head = None
    it = iter(reversed(the_list))
    while True:
        try:
            head = make_node(next(it), head)
        except StopIteration:
            return head


# **********************************************************************
# Main Program
# **********************************************************************


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    sys.stdout.flush()
    dummy = input(msg)


# Main program

if __name__ == '__main__':
    # Printable name for this test suite
    test_suite_name = "Assignment 3 Functions - CS 311 Assn 3, Exs A-D"

    # Run tests & print results
    print(f"BEGIN tests for {test_suite_name}")
    unittest.main(exit=False)  # This call will return
    print(f"END tests for {test_suite_name}")

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

