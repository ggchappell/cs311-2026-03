#!/usr/bin/env python3
# lazyseq_test.py
# Glenn G. Chappell
# 2026-09-11
"""Test program for class LazySeq.
For CS 311 Fall 2026

For Assignment 2, Exercise A
Requires lazyseq.py
"""

# Import for code to be tested
import lazyseq    # For .LazySeq

# Import for testing framework
import unittest   # For .TestCase, .main

# Other imports for test suite
import sys        # For .stdout
import itertools  # For .count, .islice


# **********************************************************************
# Helper Code
# **********************************************************************


class IterRaise:
    """Helper for TestExceptions. __iter__ raises a given exception."""

    def __init__(self, exc):
        """Given exception is raised by __iter__."""

        self._exc = exc

    def __iter__(self):
        """Raise saved exception."""

        raise self._exc


# **********************************************************************
# Test Cases
# **********************************************************************


class TestFuncReturnTypes(unittest.TestCase):

    def test_init(self):
        ob1 = lazyseq.LazySeq()

        self.assertIsInstance(ob1, lazyseq.LazySeq)

    def test_add(self):
        ob1 = lazyseq.LazySeq()

        self.assertIs(ob1.add(1), None)

    def test_add_from_iterable(self):
        ob1 = lazyseq.LazySeq()

        self.assertIs(ob1.add_from_iterable([]), None)

    def test_add_from_iterable_now(self):
        ob1 = lazyseq.LazySeq()

        self.assertIs(ob1.add_from_iterable_now([]), None)

    def test_skip(self):
        ob1 = lazyseq.LazySeq()

        self.assertIs(ob1.skip(1), None)

    def test_clear(self):
        ob1 = lazyseq.LazySeq()

        self.assertIs(ob1.clear(), None)

    def test_iter(self):
        ob1 = lazyseq.LazySeq()
        it1 = ob1.__iter__()
        attr1 = getattr(it1, "__next__", None)
        attr2 = getattr(it1, "__iter__", None)

        self.assertTrue(callable(attr1))
        self.assertTrue(callable(attr2))


class TestBasic(unittest.TestCase):

    def test_init_list_empty(self):
        arg = []
        ob1 = lazyseq.LazySeq(arg)

        self.assertEqual(list(ob1), arg)

    def test_init_list_small(self):
        arg = [2, True, "x"]
        ob1 = lazyseq.LazySeq(arg)

        self.assertEqual(list(ob1), arg)

    def test_init_list_large(self):
        arg = [5] * 10000000
        ob1 = lazyseq.LazySeq(arg)

        self.assertEqual(list(ob1), arg)

    def test_init_range_empty(self):
        arg = range(0)
        ob1 = lazyseq.LazySeq(arg)

        self.assertEqual(list(ob1), list(arg))

    def test_init_range_small(self):
        arg = range(4)
        ob1 = lazyseq.LazySeq(arg)

        self.assertEqual(list(ob1), list(arg))

    def test_init_range_large(self):
        arg = range(10000000)
        ob1 = lazyseq.LazySeq(arg)

        self.assertEqual(list(ob1), list(arg))


class TestAdd(unittest.TestCase):

    def test_init_empty_add_1(self):
        arg = []
        to_add = "x"
        ob1 = lazyseq.LazySeq(arg)
        ob1.add(to_add)

        self.assertEqual(list(ob1), arg + [to_add])

    def test_init_small_add_1(self):
        arg = [2, 8, 7]
        to_add = "x"
        ob1 = lazyseq.LazySeq(arg)
        ob1.add(to_add)

        self.assertEqual(list(ob1), arg + [to_add])

    def test_init_empty_add_multiple(self):
        arg = []
        to_add = "x"
        num_adds = 10
        ob1 = lazyseq.LazySeq(arg)
        for _ in range(num_adds):
            ob1.add(to_add)

        self.assertEqual(list(ob1), arg + [to_add]*num_adds)

    def test_init_small_add_multiple(self):
        arg = ["a", "b", "c"]
        to_add = "3"
        num_adds = 100
        ob1 = lazyseq.LazySeq(arg)
        for _ in range(num_adds):
            ob1.add(to_add)

        self.assertEqual(list(ob1), arg + [to_add]*num_adds)


class TestAddFromIterable(unittest.TestCase):

    def test_init_empty_afi_list(self):
        arg = []
        to_afi = [1, 8, 4]
        ob1 = lazyseq.LazySeq(arg)
        ob1.add_from_iterable(to_afi)

        self.assertEqual(list(ob1), arg + to_afi)

    def test_init_small_afi_range(self):
        arg = [12, 9, 3]
        to_afi = range(2, 3000, 3)
        ob1 = lazyseq.LazySeq(arg)
        ob1.add_from_iterable(to_afi)

        self.assertEqual(list(ob1), arg + list(to_afi))

    def test_init_small_afi_count(self):
        arg = [12, 9, 3]
        to_afi = itertools.count(15, 4)
        to_afi2 = itertools.count(15, 4)
        ob1 = lazyseq.LazySeq(arg)
        ob1.add_from_iterable(to_afi)

        sz = 10
        self.assertEqual(
            list(itertools.islice(ob1, sz)),
            list(itertools.islice(itertools.chain(arg, to_afi2), sz)))


class TestAddFromIterableNow(unittest.TestCase):

    def test_init_empty_afi_list(self):
        arg = []
        to_afi = [1, 8, 4]
        ob1 = lazyseq.LazySeq(arg)
        ob1.add_from_iterable_now(to_afi)

        self.assertEqual(list(ob1), arg + to_afi)

    def test_init_small_afi_range(self):
        arg = [12, 9, 3]
        to_afi = range(2, 3000, 3)
        ob1 = lazyseq.LazySeq(arg)
        ob1.add_from_iterable_now(to_afi)

        self.assertEqual(list(ob1), arg + list(to_afi))


class TestSkip(unittest.TestCase):

    def test_1_skip(self):
        arg = [1,2,3,4,1,2,3,4]
        to_skip1 = 2
        ob1 = lazyseq.LazySeq(arg)
        ob1.skip(to_skip1)
        expected = [1,3,4,1,3,4]

        self.assertEqual(list(ob1), expected)

    def test_multiple_skip(self):
        arg = [1,2,3,4,1,2,3,4]
        to_skip1 = 2
        to_skip2 = 4
        to_skip3 = 1
        ob1 = lazyseq.LazySeq(arg)
        ob1.skip(to_skip1)
        ob1.skip(to_skip2)
        ob1.skip(to_skip3)
        expected = [3,3]

        self.assertEqual(list(ob1), expected)

    def test_skip_add(self):
        arg = [1,2,3,4,1,2,3,4]
        to_skip1 = 2
        ob1 = lazyseq.LazySeq(arg)
        ob1.skip(to_skip1)
        ob1.add(to_skip1)
        expected = [1,3,4,1,3,4,2]

        self.assertEqual(list(ob1), expected)


class TestClear(unittest.TestCase):

    def test_clear(self):
        arg = [1,2,3,4,1,2,3,4]
        ob1 = lazyseq.LazySeq(arg)
        ob1.clear()
        expected = []

        self.assertEqual(list(ob1), expected)

    def test_clear_add(self):
        arg = [1,2,3,4,1,2,3,4]
        to_add = 5
        ob1 = lazyseq.LazySeq(arg)
        ob1.clear()
        ob1.add(to_add)
        expected = [to_add]

        self.assertEqual(list(ob1), expected)


class TestComplex(unittest.TestCase):

    def test_cplx1(self):
        ob1 = lazyseq.LazySeq([1,7,4,6,5,3,4,4,1])
        ob1.add(2)
        ob1.add_from_iterable(range(5))
        ob1.skip(4)
        ob1.skip(1)
        ob1.add_from_iterable(range(2))
        expected = [7,6,5,3,2,0,2,3,0,1]

        self.assertEqual(list(ob1), expected)

    def test_cplx2(self):
        ob1 = lazyseq.LazySeq(range(100))
        ob1.add(3)
        ob1.clear()
        ob1.add(7)
        ob1.add_from_iterable([4]*100)
        ob1.add(6)
        ob1.skip(4)
        ob1.add_from_iterable_now(range(100))
        expected = [7, 6] + list(range(100))

        self.assertEqual(list(ob1), expected)


class TestExceptions(unittest.TestCase):

    def test_pass_noniterable1(self):
        noniterable1 = 42

        with self.assertRaises(TypeError):
            ob1 = lazyseq.LazySeq(noniterable1)

    def test_pass_noniterable2(self):
        noniterable1 = 42
        ob1 = lazyseq.LazySeq([1,2,3])

        with self.assertRaises(TypeError):
            ob1.add_from_iterable(noniterable1)

    def test_pass_noniterable3(self):
        noniterable1 = 42
        ob1 = lazyseq.LazySeq([1,2,3])

        with self.assertRaises(TypeError):
            ob1.add_from_iterable_now(noniterable1)

    def test_now_pass_raising_iterable1(self):
        exc1 = KeyboardInterrupt("abc")
        raising_iterable1 = IterRaise(exc1)
        ob1 = lazyseq.LazySeq([1,2,3])

        with self.assertRaises(KeyboardInterrupt):
            ob1.add_from_iterable_now(raising_iterable1)

    def test_now_pass_raising_iterable2(self):
        exc1 = AssertionError("abc")
        raising_iterable1 = IterRaise(exc1)
        ob1 = lazyseq.LazySeq([1,2,3])

        with self.assertRaises(AssertionError):
            ob1.add_from_iterable_now(raising_iterable1)

    def test_now_pass_raising_iterable3(self):
        exc1 = ValueError("abc")
        raising_iterable1 = IterRaise(exc1)
        ob1 = lazyseq.LazySeq([1,2,3])

        with self.assertRaises(RuntimeError):
            ob1.add_from_iterable_now(raising_iterable1)


class TestIterateTwice(unittest.TestCase):

    def test_cplx1(self):
        ob1 = lazyseq.LazySeq([1,7])
        ob1.clear()
        ob1.add(2)
        ob1.add(1)
        ob1.add_from_iterable(range(3))
        ob1.skip(1)
        ob1.add_from_iterable_now(range(2))
        expected = [2,0,2,0,1]

        self.assertEqual(list(ob1), expected)
        self.assertIsInstance(list(ob1), list)
            # The point of the above is that no exception is raised.


# **********************************************************************
# Helper Funcs & Main Program
# **********************************************************************


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    sys.stdout.flush()
    dummy = input(msg)


# Main program

if __name__ == '__main__':
    # Printable name for this test suite
    test_suite_name = "class Player - CS 311 Assn 1, Ex A"

    # Run tests & print results
    print(f"BEGIN tests for {test_suite_name}")
    unittest.main(exit=False)  # This call will return
    print(f"END tests for {test_suite_name}")

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

