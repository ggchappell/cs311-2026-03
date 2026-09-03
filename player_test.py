#!/usr/bin/env python3
# player_test.py
# Glenn G. Chappell
# 2026-09-02
"""Test program for class Player.
For CS 311 Fall 2026

For Assignment 1, Exercise A
Requires player.py
"""

# Import for code to be tested
import player    # For .Player

# Import for testing framework
import unittest  # For .TestCase, .main

# Other imports for test suite
import sys       # For .stdout
import copy      # For .deepcopy


# **********************************************************************
# Test Cases
# **********************************************************************


class TestFuncReturnTypes(unittest.TestCase):

    ob1 = player.Player("", "", 0)
    ob2 = player.Player("", "", 0)

    def test_init(self):
        self.assertIsInstance(self.ob1, player.Player)

    def test_get_real_name(self):
        self.assertIsInstance(self.ob1.get_real_name(), str)

    def test_get_user_name(self):
        self.assertIsInstance(self.ob1.get_user_name(), str)

    def test_get_games(self):
        self.assertIsInstance(self.ob1.get_games(), int)

    def test_set_real_name(self):
        self.assertIs(self.ob1.set_real_name(""), None)

    def test_set_user_name(self):
        self.assertIs(self.ob1.set_user_name(""), None)

    def test_set_games(self):
        self.assertIs(self.ob1.set_games(0), None)

    def test_inactive(self):
        self.assertIsInstance(self.ob1.inactive(), bool)

    def test_iadd(self):
        self.ob1 += 1

        self.assertIsInstance(self.ob1, player.Player)

    def test_isub(self):
        self.ob1 -= 1

        self.assertIsInstance(self.ob1, player.Player)

    def test_eq(self):
        self.assertIsInstance(self.ob1 == self.ob2, bool)

    def test_ne(self):
        self.assertIsInstance(self.ob1 != self.ob2, bool)

    def test_str(self):
        self.assertIsInstance(self.ob1.__str__(), str)

    def test_repr(self):
        self.assertIsInstance(self.ob1.__repr__(), str)


class TestInitGetSet(unittest.TestCase):

    ob1 = player.Player("a", "b", 3)
    ob2 = None

    def test_initial_vals(self):
        self.assertEqual(self.ob1.get_real_name(), "a")
        self.assertEqual(self.ob1.get_user_name(), "b")
        self.assertEqual(self.ob1.get_games(), 3)

    def test_set_real_name(self):
        self.ob2 = copy.deepcopy(self.ob1)
        self.ob2.set_real_name("a2")

        self.assertEqual(self.ob2.get_real_name(), "a2")
        self.assertEqual(self.ob2.get_user_name(), "b")
        self.assertEqual(self.ob2.get_games(), 3)

    def test_set_user_name(self):
        self.ob2 = copy.deepcopy(self.ob1)
        self.ob2.set_user_name("b2")

        self.assertEqual(self.ob2.get_real_name(), "a")
        self.assertEqual(self.ob2.get_user_name(), "b2")
        self.assertEqual(self.ob2.get_games(), 3)

    def test_set_games(self):
        self.ob2 = copy.deepcopy(self.ob1)
        self.ob2.set_games(32)

        self.assertEqual(self.ob2.get_real_name(), "a")
        self.assertEqual(self.ob2.get_user_name(), "b")
        self.assertEqual(self.ob2.get_games(), 32)


class TestIaddIsub(unittest.TestCase):

    ob1 = player.Player("a", "b", 3)
    ob2 = None

    def test_iadd_pos(self):
        self.ob2 = copy.deepcopy(self.ob1)
        self.ob2_orig = self.ob2
        self.ob2 += 5

        self.assertIs(self.ob2, self.ob2_orig)  # Still same object?
        self.assertEqual(self.ob2.get_real_name(), "a")
        self.assertEqual(self.ob2.get_user_name(), "b")
        self.assertEqual(self.ob2.get_games(), 8)

    def test_iadd_neg(self):
        self.ob2 = copy.deepcopy(self.ob1)
        self.ob2_orig = self.ob2
        self.ob2 += -2

        self.assertIs(self.ob2, self.ob2_orig)  # Still same object?
        self.assertEqual(self.ob2.get_real_name(), "a")
        self.assertEqual(self.ob2.get_user_name(), "b")
        self.assertEqual(self.ob2.get_games(), 1)

    def test_isub_pos(self):
        self.ob2 = copy.deepcopy(self.ob1)
        self.ob2_orig = self.ob2
        self.ob2 -= 2

        self.assertIs(self.ob2, self.ob2_orig)  # Still same object?
        self.assertEqual(self.ob2.get_real_name(), "a")
        self.assertEqual(self.ob2.get_user_name(), "b")
        self.assertEqual(self.ob2.get_games(), 1)

    def test_isub_neg(self):
        self.ob2 = copy.deepcopy(self.ob1)
        self.ob2_orig = self.ob2
        self.ob2 -= -5

        self.assertIs(self.ob2, self.ob2_orig)  # Still same object?
        self.assertEqual(self.ob2.get_real_name(), "a")
        self.assertEqual(self.ob2.get_user_name(), "b")
        self.assertEqual(self.ob2.get_games(), 8)


class TestInactive(unittest.TestCase):

    ob1 = player.Player("a", "b", 0)
    ob2 = player.Player("x", "y", 2)

    def test_original_value_inactive(self):
        self.assertTrue(self.ob1.inactive())

    def test_original_value_active(self):
        self.assertFalse(self.ob2.inactive())

    def test_value_chgd1_inactive(self):
        self.ob1 += 1

        self.assertFalse(self.ob1.inactive())

    def test_value_chgd1_inactive(self):
        self.ob2 -= 2

        self.assertTrue(self.ob2.inactive())

    def test_value_chgd2_inactive(self):
        self.ob1 += 1
        self.ob1 -= 1

        self.assertTrue(self.ob1.inactive())

    def test_value_chgd2_inactive(self):
        self.ob2 -= 2
        self.ob2 += 2

        self.assertFalse(self.ob2.inactive())


class TestStrRepr(unittest.TestCase):

    ob1 = player.Player("abcde", "bcdef", 100)
    ob2 = player.Player("", "", 0)

    def test_first_object(self):
        expected = "abcde (bcdef): 100"

        self.assertEqual(self.ob1.__str__(), expected)
        self.assertEqual(self.ob1.__repr__(), expected)

    def test_second_object(self):
        expected = " (): 0"

        self.assertEqual(self.ob2.__str__(), expected)
        self.assertEqual(self.ob2.__repr__(), expected)


class TestEqNe(unittest.TestCase):

    ob1 = player.Player("abc", "def", 100)  # Base
    ob2 = player.Player("abc", "def", 100)  # Same
    ob3 = player.Player("ABC", "def", 100)  # Different real name
    ob4 = player.Player("abc", "DEF", 100)  # Different username
    ob5 = player.Player("abc", "def", 222)  # Different no. of games

    def test_equality(self):
        self.assertTrue(self.ob1 == self.ob1)
        self.assertTrue(self.ob1 == self.ob2)
        self.assertTrue(self.ob2 == self.ob1)
        self.assertFalse(self.ob1 == self.ob3)
        self.assertFalse(self.ob3 == self.ob1)
        self.assertFalse(self.ob1 == self.ob4)
        self.assertFalse(self.ob4 == self.ob1)
        self.assertFalse(self.ob1 == self.ob5)
        self.assertFalse(self.ob5 == self.ob1)

    def test_inequality(self):
        self.assertFalse(self.ob1 != self.ob1)
        self.assertFalse(self.ob1 != self.ob2)
        self.assertFalse(self.ob2 != self.ob1)
        self.assertTrue(self.ob1 != self.ob3)
        self.assertTrue(self.ob3 != self.ob1)
        self.assertTrue(self.ob1 != self.ob4)
        self.assertTrue(self.ob4 != self.ob1)
        self.assertTrue(self.ob1 != self.ob5)
        self.assertTrue(self.ob5 != self.ob1)


class TestLargeValues(unittest.TestCase):

    ob1 = player.Player("abc", "def", 100)
    ob2 = None
    long_string = "abcdefghij" * 1000000
    large_int = 123 ** 2050  # Big, but still printable

    def test_long_real_name(self):
        self.ob2 = copy.deepcopy(self.ob1)
        self.ob2.set_real_name(self.long_string)

        self.assertEqual(self.ob2.get_real_name(), self.long_string)

    def test_long_user_name(self):
        self.ob2 = copy.deepcopy(self.ob1)
        self.ob2.set_user_name(self.long_string)

        self.assertEqual(self.ob2.get_user_name(), self.long_string)

    def test_large_games(self):
        self.ob2 = copy.deepcopy(self.ob1)
        self.ob2.set_games(self.large_int)

        self.assertEqual(self.ob2.get_games(), self.large_int)


# **********************************************************************
# Helper Funcs & Main Program
# **********************************************************************


def user_pause(msg):
    """Wait for user to press ENTER."""

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

