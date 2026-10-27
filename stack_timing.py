#!/usr/bin/env python3
# stack_timing.py
# Glenn G. Chappell
# 2026-10-25
"""Timing Stack operations.
For CS 311 Fall 2026
"""


import collections  # for .deque
import queue        # for .LifoQueue


# Number of pushes & pops to do
NUM_OPS = 10_000_000


def run_ops(dataset):
    """Do NUM_OPS push & pop ops on dataset, print messages."""

    print(f"  {NUM_OPS:,} push & pop operations")
    print("  Running ... ", end="", flush=True)

    start_time = time_sec()

    if isinstance(dataset, queue.LifoQueue):
        my_push = dataset.put
        my_pop = dataset.get
    elif (isinstance(dataset, list)
      or isinstance(dataset, collections.deque)):
        my_push = dataset.append
        my_pop = dataset.pop
    else:
        raise TypeError("run_ops: queue is not of a supported type")

    for i in range(NUM_OPS):
        my_push(42)
    for i in range(NUM_OPS):
        my_pop()

    end_time = time_sec()

    print("DONE", flush=True)

    print(f"  Elapsed time: {end_time-start_time:.4g} seconds")


def time_sec():
    """Return float: time in seconds since some starting point.
    Resolution is nanoseconds, if the system provides this.
    Value increases consistently within a single program run.
    Intended for things like timing function calls.
    Not for use in determining time of day.
    """

    import time  # For .clock_gettime_ns, .CLOCK_MONOTONIC_RAW

    ns_per_sec = 1_000_000_000
    return time.clock_gettime_ns(time.CLOCK_MONOTONIC_RAW) / ns_per_sec


def user_pause(msg):
    """Print given message and wait for user to press ENTER."""

    assert isinstance(msg, str)

    print("", end="", flush=True)
    _ = input(msg)


# Main program
# Times Stack operations using different implementations

if __name__ == "__main__":

    # ***** Initial Message *****

    print("Timing Stack Operations")

    # ***** list *****

    print()
    print("list")
    dataset = list()
    run_ops(dataset)

    # ***** collections.deque *****

    print()
    print("collections.deque")
    dataset = collections.deque()
    run_ops(dataset)

    # ***** queue.LifoQueue *****

    print()
    print("queue.LifoQueue")
    dataset = queue.LifoQueue()
    run_ops(dataset)

    # ***** Done *****

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

