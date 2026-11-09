#!/usr/bin/env python3
# treesort_test.py
# Glenn G. Chappell
# 2026-11-09
"""Test program for function treesort.
For CS 311 Fall 2026

For Assignment 7, Exercise A
Requires treesort.py
"""

# Import for code to be tested
import treesort     # For .treesort

# Import for testing framework
import unittest     # For .TestCase, .main

# Other imports for test suite
import collections  # For .deque


# **********************************************************************
# Test Cases
# **********************************************************************


class Test00SmallListInt(unittest.TestCase):

    def test00_empty(self):
        data1 = []

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test01_size_1(self):
        data1 = [1]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test02_size_2_a(self):
        data1 = [1, 2]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test03_size_2_b(self):
        data1 = [2, 1]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test04_size_2_c(self):
        data1 = [1, 1]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test05_size_3_a(self):
        data1 = [1, 2, 3]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test06_size_3_b(self):
        data1 = [1, 3, 2]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test07_size_3_c(self):
        data1 = [2, 1, 3]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test08_size_3_d(self):
        data1 = [2, 3, 1]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test09_size_3_e(self):
        data1 = [3, 1, 2]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test10_size_3_f(self):
        data1 = [3, 2, 1]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test11_size_3_g(self):
        data1 = [1, 2, 2]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test12_size_3_h(self):
        data1 = [2, 1, 2]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test13_size_3_i(self):
        data1 = [2, 2, 1]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test14_size_3_j(self):
        data1 = [2, 1, 1]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test15_size_3_k(self):
        data1 = [1, 2, 1]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test16_size_3_l(self):
        data1 = [1, 1, 2]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test17_size_3_m(self):
        data1 = [1, 1, 1]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)


class Test01SmallDequeStr(unittest.TestCase):

    def test00_empty(self):
        data1 = []

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test01_size_1(self):
        data1 = ["1"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test02_size_2_a(self):
        data1 = ["1", "2"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test03_size_2_b(self):
        data1 = ["2", "1"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test04_size_2_c(self):
        data1 = ["1", "1"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test05_size_3_a(self):
        data1 = ["1", "2", "3"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test06_size_3_b(self):
        data1 = ["1", "3", "2"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test07_size_3_c(self):
        data1 = ["2", "1", "3"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test08_size_3_d(self):
        data1 = ["2", "3", "1"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test09_size_3_e(self):
        data1 = ["3", "1", "2"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test10_size_3_f(self):
        data1 = ["3", "2", "1"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test11_size_3_g(self):
        data1 = ["1", "2", "2"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test12_size_3_h(self):
        data1 = ["2", "1", "2"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test13_size_3_i(self):
        data1 = ["2", "2", "1"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test14_size_3_j(self):
        data1 = ["2", "1", "1"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test15_size_3_k(self):
        data1 = ["1", "2", "1"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test16_size_3_l(self):
        data1 = ["1", "1", "2"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)

    def test17_size_3_m(self):
        data1 = ["1", "1", "1"]

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)


class Test02Indices(unittest.TestCase):

    def test00_indices(self):
        data1 = [9,7,5,3,1,8,6,4,2,0]

        data2 = data1.copy()
        treesort.treesort(data2, 3, 8)
        data3 = data1[:3] + sorted(data1[3:8]) + data1[8:]

        self.assertEqual(data2, data3)


class Test03Stability(unittest.TestCase):

    def test00_stable_size_9(self):
        data1 = [Comp(3,3),Comp(2,2),Comp(1,1),
                 Comp(3,1),Comp(2,3),Comp(1,2),
                 Comp(3,2),Comp(2,1),Comp(1,3)]

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)


class Test04Long(unittest.TestCase):

    def test00_long(self):
        bignum = 1_000
        data1 = (list(range(bignum-1,-1,-2))
               + list(range(bignum-2,-1,-2)))

        data2 = data1.copy()
        treesort.treesort(data2)
        data3 = sorted(data1)

        self.assertEqual(data2, data3)

    def test01_longer(self):
        """Much longer range, but designed to avoid stack overflow."""

        data1 = collections.deque()
        exponent = 17  # Data will hold values 1 .. 2**exponent-1
        start = 1
        skip = 2
        end = 2**exponent
        for i in range(exponent):
            for v in range(start, end, skip):
                data1.appendleft(v)
            start *= 2
            skip *= 2

        data2 = collections.deque(data1)
        treesort.treesort(data2)
        data3 = collections.deque(sorted(data1))

        self.assertEqual(data2, data3)


# **********************************************************************
# Helper Code
# **********************************************************************


class Comp:
    """Class with comparisons: <, ==.
    """

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __lt__(self, other):
        return self._a < other._a

    def __eq__(self, other):
        if not isinstance(other, Comp):
            return False
        return self._a == other._a and self._b == other._b

    def __copy__(self):
        return Comp(self._a, self._b)

    def __repr__(self):
        return "Comp(" + repr(self._a) + "," + repr(self._b) + ")"

    def __str__(self):
        return repr(self)


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
    test_suite_name = "function treesort - CS 311 Assn 7, Ex A"

    # Run tests & print results
    print(f"BEGIN tests for {test_suite_name}")
    unittest.main(exit=False)  # This call will return
    print(f"END tests for {test_suite_name}")

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

