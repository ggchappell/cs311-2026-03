#!/usr/bin/env python3
# hdt_count_test.py
# Glenn G. Chappell
# 2026-09-25
"""Test program for function hdt_count.
For CS 311 Fall 2026

For Assignment 4, Exercise A
Requires hdt_count.py
"""

# Import for code to be tested
import hdt_count  # For .hdt_count

# Import for testing framework
import unittest   # For .TestCase, .main

# Other imports for test suite
import sys        # For .stdout


# **********************************************************************
# Test Cases
# **********************************************************************


class TestReturnType(unittest.TestCase):

    def test_hdt_count_return(self):
        val = hdt_count.hdt_count(4,3, 2,0, 3,2)

        self.assertIsInstance(val, int)


class TestBoards_nx1_1xn(unittest.TestCase):

    def test_all_2x1(self):
        self.assertEqual(hdt_count.hdt_count(2,1, 0,0, 1,0), 1)
        self.assertEqual(hdt_count.hdt_count(2,1, 1,0, 0,0), 1)

    def test_all_1x2(self):
        self.assertEqual(hdt_count.hdt_count(1,2, 0,0, 0,1), 1)
        self.assertEqual(hdt_count.hdt_count(1,2, 0,1, 0,0), 1)

    def test_all_3x1(self):
        self.assertEqual(hdt_count.hdt_count(3,1, 0,0, 1,0), 0)
        self.assertEqual(hdt_count.hdt_count(3,1, 0,0, 2,0), 0)
        self.assertEqual(hdt_count.hdt_count(3,1, 1,0, 0,0), 0)
        self.assertEqual(hdt_count.hdt_count(3,1, 1,0, 2,0), 0)
        self.assertEqual(hdt_count.hdt_count(3,1, 2,0, 0,0), 0)
        self.assertEqual(hdt_count.hdt_count(3,1, 2,0, 1,0), 0)

    def test_all_1x3(self):
        self.assertEqual(hdt_count.hdt_count(1,3, 0,0, 0,1), 0)
        self.assertEqual(hdt_count.hdt_count(1,3, 0,0, 0,2), 0)
        self.assertEqual(hdt_count.hdt_count(1,3, 0,1, 0,0), 0)
        self.assertEqual(hdt_count.hdt_count(1,3, 0,1, 0,2), 0)
        self.assertEqual(hdt_count.hdt_count(1,3, 0,2, 0,0), 0)
        self.assertEqual(hdt_count.hdt_count(1,3, 0,2, 0,1), 0)

    def test_all_4x1(self):
        self.assertEqual(hdt_count.hdt_count(4,1, 0,0, 1,0), 1)
        self.assertEqual(hdt_count.hdt_count(4,1, 0,0, 2,0), 0)
        self.assertEqual(hdt_count.hdt_count(4,1, 0,0, 3,0), 1)
        self.assertEqual(hdt_count.hdt_count(4,1, 1,0, 0,0), 1)
        self.assertEqual(hdt_count.hdt_count(4,1, 1,0, 2,0), 0)
        self.assertEqual(hdt_count.hdt_count(4,1, 1,0, 3,0), 0)
        self.assertEqual(hdt_count.hdt_count(4,1, 2,0, 0,0), 0)
        self.assertEqual(hdt_count.hdt_count(4,1, 2,0, 1,0), 0)
        self.assertEqual(hdt_count.hdt_count(4,1, 2,0, 3,0), 1)
        self.assertEqual(hdt_count.hdt_count(4,1, 3,0, 0,0), 1)
        self.assertEqual(hdt_count.hdt_count(4,1, 3,0, 1,0), 0)
        self.assertEqual(hdt_count.hdt_count(4,1, 3,0, 2,0), 1)

    def test_all_1x4(self):
        self.assertEqual(hdt_count.hdt_count(1,4, 0,0, 0,1), 1)
        self.assertEqual(hdt_count.hdt_count(1,4, 0,0, 0,2), 0)
        self.assertEqual(hdt_count.hdt_count(1,4, 0,0, 0,3), 1)
        self.assertEqual(hdt_count.hdt_count(1,4, 0,1, 0,0), 1)
        self.assertEqual(hdt_count.hdt_count(1,4, 0,1, 0,2), 0)
        self.assertEqual(hdt_count.hdt_count(1,4, 0,1, 0,3), 0)
        self.assertEqual(hdt_count.hdt_count(1,4, 0,2, 0,0), 0)
        self.assertEqual(hdt_count.hdt_count(1,4, 0,2, 0,1), 0)
        self.assertEqual(hdt_count.hdt_count(1,4, 0,2, 0,3), 1)
        self.assertEqual(hdt_count.hdt_count(1,4, 0,3, 0,0), 1)
        self.assertEqual(hdt_count.hdt_count(1,4, 0,3, 0,1), 0)
        self.assertEqual(hdt_count.hdt_count(1,4, 0,3, 0,2), 1)

    def test_various_nx1_n_gt_4(self):
        self.assertEqual(hdt_count.hdt_count(10,1,  0,0,  9,0), 1)
        self.assertEqual(hdt_count.hdt_count(50,1,  1,0,  0,0), 1)
        self.assertEqual(hdt_count.hdt_count(60,1,  1,0,  2,0), 0)
        self.assertEqual(hdt_count.hdt_count(60,1, 24,0, 25,0), 1)
        self.assertEqual(hdt_count.hdt_count(98,1, 97,0,  0,0), 1)
        self.assertEqual(hdt_count.hdt_count(99,1, 98,0, 97,0), 0)

    def test_various_1xn_n_gt_4(self):
        self.assertEqual(hdt_count.hdt_count(1,12, 0,11, 0, 0), 1)
        self.assertEqual(hdt_count.hdt_count(1,48, 0, 0, 0, 1), 1)
        self.assertEqual(hdt_count.hdt_count(1,62, 0,38, 0,37), 0)
        self.assertEqual(hdt_count.hdt_count(1,62, 0,37, 0,36), 1)
        self.assertEqual(hdt_count.hdt_count(1,98, 0,96, 0,97), 1)
        self.assertEqual(hdt_count.hdt_count(1,99, 0, 0, 0,98), 0)


class TestBoards_Small(unittest.TestCase):

    def test_various_small(self):
        self.assertEqual(hdt_count.hdt_count(2,4, 1,0, 0,2),  1)
        self.assertEqual(hdt_count.hdt_count(5,2, 1,0, 3,1),  1)
        self.assertEqual(hdt_count.hdt_count(3,4, 2,0, 2,1),  7)
        self.assertEqual(hdt_count.hdt_count(3,6, 1,2, 2,4),  3)
        self.assertEqual(hdt_count.hdt_count(4,5, 1,2, 2,3),  0)
        self.assertEqual(hdt_count.hdt_count(5,4, 4,1, 0,0), 16)
        self.assertEqual(hdt_count.hdt_count(3,7, 1,1, 1,2),  0)


class TestBoards_FibonacciFun(unittest.TestCase):

    def test_fibonacci_results(self):
        self.assertEqual(hdt_count.hdt_count( 1,2, 0,0, 0,1),    1)
        self.assertEqual(hdt_count.hdt_count( 2,2, 0,0, 0,1),    1)
        self.assertEqual(hdt_count.hdt_count( 3,2, 0,0, 0,1),    2)
        self.assertEqual(hdt_count.hdt_count( 4,2, 0,0, 0,1),    3)
        self.assertEqual(hdt_count.hdt_count( 5,2, 0,0, 0,1),    5)
        self.assertEqual(hdt_count.hdt_count( 6,2, 0,0, 0,1),    8)
        self.assertEqual(hdt_count.hdt_count( 7,2, 0,0, 0,1),   13)
        self.assertEqual(hdt_count.hdt_count( 8,2, 0,0, 0,1),   21)
        self.assertEqual(hdt_count.hdt_count( 9,2, 0,0, 0,1),   34)
        self.assertEqual(hdt_count.hdt_count(10,2, 0,0, 0,1),   55)
        self.assertEqual(hdt_count.hdt_count(11,2, 0,0, 0,1),   89)
        self.assertEqual(hdt_count.hdt_count(12,2, 0,0, 0,1),  144)
        self.assertEqual(hdt_count.hdt_count(13,2, 0,0, 0,1),  233)
        self.assertEqual(hdt_count.hdt_count(14,2, 0,0, 0,1),  377)
        self.assertEqual(hdt_count.hdt_count(15,2, 0,0, 0,1),  610)
        self.assertEqual(hdt_count.hdt_count(16,2, 0,0, 0,1),  987)
        self.assertEqual(hdt_count.hdt_count(17,2, 0,0, 0,1), 1597)


class TestBoards_Larger(unittest.TestCase):

    def test_various_larger(self):
        self.assertEqual(hdt_count.hdt_count( 2,11, 0,4, 1,4),   65)
        self.assertEqual(hdt_count.hdt_count(12, 2, 7,0, 7,1),  105)
        self.assertEqual(hdt_count.hdt_count( 4, 7, 1,1, 3,4),   91)
        self.assertEqual(hdt_count.hdt_count(10, 3, 2,1, 6,2),   12)
        self.assertEqual(hdt_count.hdt_count( 4, 8, 1,0, 3,6),    0)
        self.assertEqual(hdt_count.hdt_count( 8, 4, 5,3, 1,0),  175)
        self.assertEqual(hdt_count.hdt_count( 6, 6, 3,0, 4,0), 1276)
        self.assertEqual(hdt_count.hdt_count( 2,19, 0,9, 1,9), 3025)
        self.assertEqual(hdt_count.hdt_count( 5, 8, 0,0, 1,0), 6533)


class TestBoards_SlideExamples(unittest.TestCase):

    def test_examples_from_slides(self):
        self.assertEqual(hdt_count.hdt_count(4,3, 2,0, 3,2),    4)
        self.assertEqual(hdt_count.hdt_count(3,2, 2,1, 0,0),    1)
        self.assertEqual(hdt_count.hdt_count(4,1, 1,0, 3,0),    0)
        self.assertEqual(hdt_count.hdt_count(8,5, 6,4, 7,4), 8291)


# **********************************************************************
# Helper Code
# **********************************************************************


# None


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
    test_suite_name = "function hdt_count - CS 311 Assn 4, Ex A"

    # Run tests & print results
    print(f"BEGIN tests for {test_suite_name}")
    unittest.main(exit=False)  # This call will return
    print(f"END tests for {test_suite_name}")

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

