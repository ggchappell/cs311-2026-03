#!/usr/bin/env python3
# reverser_test.py  SKELETON
# Glenn G. Chappell
# 2026-11-18
"""Test program for class Reverser.
For CS 311 Fall 2026

For Assignment 8, Exercise B
Requires reverser.py
"""

# Import for code to be tested
import reverser  # For .Reverser

# Import for testing framework
import unittest  # For .TestCase, .main

# Other imports for test suite
# None


# **********************************************************************
# Test Cases
# **********************************************************************


class TestXYZ(unittest.TestCase):
    """Dummy."""

    def test_xyz(self):
        """Dummy."""
        pass


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
    test_suite_name = "class Reverser - CS 311 Assn 8, Ex B"

    # Run tests & print results
    print(f"BEGIN tests for {test_suite_name}")
    unittest.main(exit=False)  # This call will return
    print(f"END tests for {test_suite_name}")

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

