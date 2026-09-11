#!/usr/bin/env python3
# player_test.py
# VERSION 2
# Glenn G. Chappell
# Started: 2026-09-02
# Updated: 2026-09-10
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


# **********************************************************************
# Test Cases
# **********************************************************************


class TestFuncReturnTypes(unittest.TestCase):

    def test_init(self):
        ob1 = player.Player("", "", 0)

        self.assertIsInstance(ob1, player.Player)

    def test_get_real_name(self):
        ob1 = player.Player("", "", 0)

        self.assertIsInstance(ob1.get_real_name(), str)

    def test_get_user_name(self):
        ob1 = player.Player("", "", 0)

        self.assertIsInstance(ob1.get_user_name(), str)

    def test_get_games(self):
        ob1 = player.Player("", "", 0)

        self.assertIsInstance(ob1.get_games(), int)

    def test_set_real_name(self):
        ob1 = player.Player("", "", 0)

        self.assertIs(ob1.set_real_name(""), None)

    def test_set_user_name(self):
        ob1 = player.Player("", "", 0)

        self.assertIs(ob1.set_user_name(""), None)

    def test_set_games(self):
        ob1 = player.Player("", "", 0)

        self.assertIs(ob1.set_games(0), None)

    def test_inactive(self):
        ob1 = player.Player("", "", 0)

        self.assertIsInstance(ob1.inactive(), bool)

    def test_iadd(self):
        ob1 = player.Player("", "", 0)
        ob1 += 1

        self.assertIsInstance(ob1, player.Player)

    def test_isub(self):
        ob1 = player.Player("", "", 0)
        ob1 -= 0

        self.assertIsInstance(ob1, player.Player)

    def test_eq(self):
        ob1 = player.Player("", "", 0)
        ob2 = player.Player("", "", 0)

        self.assertIsInstance(ob1 == ob2, bool)

    def test_ne(self):
        ob1 = player.Player("", "", 0)
        ob2 = player.Player("", "", 0)

        self.assertIsInstance(ob1 != ob2, bool)

    def test_str(self):
        ob1 = player.Player("", "", 0)

        self.assertIsInstance(ob1.__str__(), str)

    def test_repr(self):
        ob1 = player.Player("", "", 0)

        self.assertIsInstance(ob1.__repr__(), str)


class TestInitGetSet(unittest.TestCase):

    def test_initial_vals(self):
        ob1 = player.Player("a", "b", 3)

        self.assertEqual(ob1.get_real_name(), "a")
        self.assertEqual(ob1.get_user_name(), "b")
        self.assertEqual(ob1.get_games(), 3)

    def test_set_real_name(self):
        ob1 = player.Player("a", "b", 3)
        ob1.set_real_name("a2")

        self.assertEqual(ob1.get_real_name(), "a2")
        self.assertEqual(ob1.get_user_name(), "b")
        self.assertEqual(ob1.get_games(), 3)

    def test_set_user_name(self):
        ob1 = player.Player("a", "b", 3)
        ob1.set_user_name("b2")

        self.assertEqual(ob1.get_real_name(), "a")
        self.assertEqual(ob1.get_user_name(), "b2")
        self.assertEqual(ob1.get_games(), 3)

    def test_set_games(self):
        ob1 = player.Player("a", "b", 3)
        ob1.set_games(32)

        self.assertEqual(ob1.get_real_name(), "a")
        self.assertEqual(ob1.get_user_name(), "b")
        self.assertEqual(ob1.get_games(), 32)


class TestIaddIsub(unittest.TestCase):

    def test_iadd_pos(self):
        ob1 = player.Player("a", "b", 3)
        ob1_orig = ob1
        ob1 += 5

        self.assertIs(ob1, ob1_orig)  # Still same object?
        self.assertEqual(ob1.get_real_name(), "a")
        self.assertEqual(ob1.get_user_name(), "b")
        self.assertEqual(ob1.get_games(), 8)

    def test_iadd_neg(self):
        ob1 = player.Player("a", "b", 3)
        ob1_orig = ob1
        ob1 += -2

        self.assertIs(ob1, ob1_orig)  # Still same object?
        self.assertEqual(ob1.get_real_name(), "a")
        self.assertEqual(ob1.get_user_name(), "b")
        self.assertEqual(ob1.get_games(), 1)

    def test_isub_pos(self):
        ob1 = player.Player("a", "b", 3)
        ob1_orig = ob1
        ob1 -= 2

        self.assertIs(ob1, ob1_orig)  # Still same object?
        self.assertEqual(ob1.get_real_name(), "a")
        self.assertEqual(ob1.get_user_name(), "b")
        self.assertEqual(ob1.get_games(), 1)

    def test_isub_neg(self):
        ob1 = player.Player("a", "b", 3)
        ob1_orig = ob1
        ob1 -= -5

        self.assertIs(ob1, ob1_orig)  # Still same object?
        self.assertEqual(ob1.get_real_name(), "a")
        self.assertEqual(ob1.get_user_name(), "b")
        self.assertEqual(ob1.get_games(), 8)


class TestInactive(unittest.TestCase):

    def test_original_value_inactive(self):
        ob1 = player.Player("a", "b", 0)

        self.assertTrue(ob1.inactive())

    def test_original_value_active(self):
        ob2 = player.Player("x", "y", 2)

        self.assertFalse(ob2.inactive())

    def test_value_chgd1_inactive(self):
        ob1 = player.Player("a", "b", 0)
        ob1 += 1

        self.assertFalse(ob1.inactive())

    def test_value_chgd1_inactive(self):
        ob2 = player.Player("x", "y", 2)
        ob2 -= 2

        self.assertTrue(ob2.inactive())

    def test_value_chgd2_inactive(self):
        ob1 = player.Player("a", "b", 0)
        ob1 += 1
        ob1 -= 1

        self.assertTrue(ob1.inactive())

    def test_value_chgd2_inactive(self):
        ob2 = player.Player("x", "y", 2)
        ob2 -= 2
        ob2 += 2

        self.assertFalse(ob2.inactive())


class TestStrRepr(unittest.TestCase):

    def test_first_object(self):
        ob1 = player.Player("abcde", "bcdef", 100)
        expected = "abcde (bcdef): 100"

        self.assertEqual(ob1.__str__(), expected)
        self.assertEqual(ob1.__repr__(), expected)

    def test_second_object(self):
        ob2 = player.Player("", "", 0)
        expected = " (): 0"

        self.assertEqual(ob2.__str__(), expected)
        self.assertEqual(ob2.__repr__(), expected)


class TestEqNe(unittest.TestCase):

    def test_equality(self):
        ob1 = player.Player("abc", "def", 100)  # Base
        ob2 = player.Player("abc", "def", 100)  # Same
        ob3 = player.Player("ABC", "def", 100)  # Different real name
        ob4 = player.Player("abc", "DEF", 100)  # Different username
        ob5 = player.Player("abc", "def", 222)  # Different no. of games

        self.assertTrue(ob1 == ob1)
        self.assertTrue(ob1 == ob2)
        self.assertTrue(ob2 == ob1)
        self.assertFalse(ob1 == ob3)
        self.assertFalse(ob3 == ob1)
        self.assertFalse(ob1 == ob4)
        self.assertFalse(ob4 == ob1)
        self.assertFalse(ob1 == ob5)
        self.assertFalse(ob5 == ob1)

    def test_inequality(self):
        ob1 = player.Player("abc", "def", 100)  # Base
        ob2 = player.Player("abc", "def", 100)  # Same
        ob3 = player.Player("ABC", "def", 100)  # Different real name
        ob4 = player.Player("abc", "DEF", 100)  # Different username
        ob5 = player.Player("abc", "def", 222)  # Different no. of games

        self.assertFalse(ob1 != ob1)
        self.assertFalse(ob1 != ob2)
        self.assertFalse(ob2 != ob1)
        self.assertTrue(ob1 != ob3)
        self.assertTrue(ob3 != ob1)
        self.assertTrue(ob1 != ob4)
        self.assertTrue(ob4 != ob1)
        self.assertTrue(ob1 != ob5)
        self.assertTrue(ob5 != ob1)


class TestLargeValues(unittest.TestCase):

    def test_long_real_name(self):
        ob1 = player.Player("abc", "def", 100)
        long_string = "abcdefghij" * 1000000
        ob1.set_real_name(long_string)

        self.assertEqual(ob1.get_real_name(), long_string)

    def test_long_user_name(self):
        ob1 = player.Player("abc", "def", 100)
        long_string = "abcdefghij" * 1000000
        ob1.set_user_name(long_string)

        self.assertEqual(ob1.get_user_name(), long_string)

    def test_large_games(self):
        ob1 = player.Player("abc", "def", 100)
        large_int = 123 ** 2050  # Big, but still printable
        ob1.set_games(large_int)

        self.assertEqual(ob1.get_games(), large_int)


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

