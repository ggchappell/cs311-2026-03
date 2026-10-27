#!/usr/bin/env python3
# queue_timing.py
# Glenn G. Chappell
# 2026-10-27
"""Timing Queue operations.
For CS 311 Fall 2026
"""


import collections  # for .deque
import queue        # for .SimpleQueue, .Queue
import functools    # for .partial


# Number of pushes & pops to do
NUM_OPS = 10_000_000


def run_ops(dataset):
    """Do NUM_OPS enqueue & dequeue ops on dataset, print messages."""

    if (isinstance(dataset, queue.Queue)
      or isinstance(dataset, queue.SimpleQueue)):
        my_enqueue = dataset.put
        my_dequeue = dataset.get
    elif isinstance(dataset, collections.deque):
        my_enqueue = dataset.append
        my_dequeue = dataset.popleft
    elif isinstance(dataset, list):
        my_enqueue = dataset.append
        my_dequeue = functools.partial(dataset.pop, 0)
    else:
        raise TypeError("run_ops: queue is not of a supported type")

    print(f"  {NUM_OPS:,} enqueue & dequeue operations")
    print("  Running ... ", end="", flush=True)

    start_time = time_sec()

    for i in range(NUM_OPS):
        my_enqueue(42)
    for i in range(NUM_OPS):
        my_dequeue()

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

    print("Timing Queue Operations")

    # ***** collections.deque *****

    print()
    print("collections.deque")
    dataset = collections.deque()
    run_ops(dataset)

    # ***** queue.SimpleQueue *****

    print()
    print("queue.SimpleQueue")
    dataset = queue.SimpleQueue()
    run_ops(dataset)

    # ***** queue.Queue *****

    print()
    print("queue.Queue")
    dataset = queue.Queue()
    run_ops(dataset)

    # ***** Done *****

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

