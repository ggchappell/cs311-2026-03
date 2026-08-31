#!/usr/bin/env python3
# timeofday_main.py
# Glenn G. Chappell
# 2026-08-31
"""Simple program using class TimeOfDay,
for CS 311 Fall 2026.
"""

import timeofday  # For .TimeOfDay
import sys        # For .stdout


def user_pause(msg):
    """Wait for user to press ENTER."""

    assert isinstance(msg, str)

    sys.stdout.flush()
    dummy = input(msg)


# Main program

if __name__ == "__main__":
    print("Simple program using class TimeOfDay")
    print()
    print("Each line below shows what should result,", end="")
    print(" and then what actually results.")
    print("This is NOT a thorough test program.")
    print()

    t1 = timeofday.TimeOfDay()
    t2 = timeofday.TimeOfDay(23, 59, 59)
    t3 = timeofday.TimeOfDay()

    print(f"' 0:00:00'     - '{t1}'")

    t2 += 1
    t2 += 1
    print(f"' 0:00:01'     - '{t2}'")

    t2 -= 1
    t2 -= 1
    print(f"'23:59:59'     - '{t2}'")

    hms = t1.getTime()
    print(f"'(0, 0, 0)'    - '{hms}'")

    hms = t2.getTime()
    print(f"'(23, 59, 59)' - '{hms}'")

    t2.setTime(8, 3, 59)
    t2 += 1
    t3 = t2
    print(f"' 8:04:00'     - '{t3}'")

    print(f"'17:40:07'     - '{t3+34567}'")
    print(f"'19:22:42'     - '{t3-45678}'")

    print(f"' 8:04:00'     - '{str(t3)}'")
    print(f"' 8:04:00'     - '{repr(t3)}'")

    print()
    user_pause("Press ENTER to quit ")

