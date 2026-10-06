#!/usr/bin/env python3
# quicksort1.py
# Glenn G. Chappell
# Started: 2026-10-01
# Updated: 2026-10-02
"""Sorting Demo: Quicksort (unoptimized).
For CS 311 Fall 2026
"""


# Size of large datasets
BIG_SIZE = 3_000_000

# Values in datasets range from 0 to MAX_VAL
MAX_VAL = 999_999_999


def quicksort(container, index1=None, index2=None):
    """Do Quicksort (unoptimized) on given range.
    Range to be sorted is [container[index1], container[index2]),
    or the whole container if index1, index2 are not passed.

    Uses h_partition.

    Pre:
    * Container is an indexable sequence.
    * If index1, index2 are both given, then:
      * index1 and index2 have type int.
      * index1 <= index2.
      * Integers in [index1, index2) are valid indices for container.
    """

    if index1 is None:
        index1 = 0
    assert isinstance(index1, int)
    if index2 is None:
        index2 = len(container)
    assert isinstance(index2, int)
    assert index2 >= index1

    # BASE CASE

    if index2 - index1 <= 1:  # Size is 0 or 1
        return

    # RECURSIVE CASE

    # Simple pivot choice: let the pivot be the first item
    pivot_index = index1

    # Do partition
    assert index1 <= pivot_index < index2
    pivot_index = h_partition(container, index1, index2, pivot_index)
    assert index1 <= pivot_index < index2

    # Two recursive sorts
    quicksort(container, index1, pivot_index)
    quicksort(container, pivot_index+1, index2)
        # Range does not include the pivot


def h_partition(container, index1, index2, pivot_index):
    """Do Hoare Partition algorithm on given range with given pivot.
    Range is [container[index1], container[index2]).
    Pivot is container[pivot_index].
    New index of pivot is returned.

    Pre:
    * Container is an indexable sequence.
    * index1, index2, pivot_index have type int.
    * index1 <= pivot_index < index2.
    * Integers in [index1, index2) are valid indices for container.
    """

    assert isinstance(index1, int)
    assert isinstance(index2, int)
    assert isinstance(pivot_index, int)
    assert index1 <= pivot_index < index2

    # Put the pivot at the start of the list
    if index1 != pivot_index:
        container[index1], container[pivot_index] = (
            container[pivot_index], container[index1])

    # index1 is now the index of the pivot

    # Index left: all items before it have !(PIVOT < ITEM)
    left = index1+1
    # Index right: all items after it have !(ITEM < PIVOT)
    right = index2-1

    # In the loop below, we stop when items before left + items
    #  after right are the entire list.
    while left <= right:
        # Move left & right in as far as we can
        while (left <= right
               and not(container[index1] < container[left])):
            left += 1
        while (left <= right
               and not(container[right] < container[index1])):
            right -= 1

        # If left & right have not collided, swap their items
        if left < right:
            container[left], container[right] = (
                container[right], container[left])
            left += 1
            right -= 1

    assert index1 <= right < index2
    assert right+1 == left

    # Return new pivot position for caller, first putting pivot there
    pivot_index = right
    if index1 != pivot_index:
        container[index1], container[pivot_index] = (
            container[pivot_index], container[index1])
    return pivot_index


def do_sort(container):
    """Wrapper func for our sort. Sorts given range with messages before
    & after. Prints elapsed time.
    """

    # Message: before
    print("  Before:")
    print(f"    {iter_str(container, 75)}")
    print("  Sorting ... ", end="", flush=True)

    # Get starting time
    starttime = time_sec()

    # *********************************************************
    # * THE FOLLOWING MUST BE THE APPROPRIATE SORTING CALL!!! *
    # *********************************************************
    quicksort(container)

    # Get ending time
    endtime = time_sec()

    # Check correctness of sort
    for i in range(len(container)-1):
        assert container[i] <= container[i+1]

    # Message: after
    print("DONE")
    print(f"  Elapsed time: {endtime-starttime:.4g} (sec)")

    print("  After:")
    print(f"    {iter_str(container, 75)}")


def try_sort_small():
    """Call do_sort on small dataset.
    Values in [0, MAX_VAL (global)].
    """

    # Initial message
    print("Sorting trial: Small dataset")

    # Make dataset
    print("Creating dataset ... ", end="", flush=True)
    data = [123456, 34, 0, 56, 2, 654321, 123, 1, 0, 99]
    for i in range(len(data)):
        data[i] %= (1+MAX_VAL)
    for val in data:
        assert 0 <= val <= MAX_VAL
    print("DONE")
    print(f"Size = {len(data):,}")
    print()

    # Sort
    do_sort(data)


def try_sort_nearly_sorted1():
    """Call do_sort on type 1 nearly sorted data.
    Type 1 = all items close to their proper spots.
    Size is BIG_SIZE (global). Values in [0, MAX_VAL (global)].
    """

    # Initial message
    print("Sorting trial: Nearly sorted type 1")
    print("  (all items close to proper spots)")

    # Make dataset
    print("Creating dataset ... ", end="", flush=True)
    data = [ (i+3-2*(i%4)) * MAX_VAL // BIG_SIZE
             for i in range(BIG_SIZE) ]
    assert len(data) == BIG_SIZE
    for val in data:
        assert 0 <= val <= MAX_VAL
    print("DONE")
    print(f"Size = {len(data):,}")
    print()

    # Sort
    do_sort(data)


def try_sort_nearly_sorted2():
    """Call do_sort on type 2 nearly sorted data.
    Type 2 = few items out of order.
    Size is BIG_SIZE (global). Values in [0, MAX_VAL (global)].
    """

    # Initial message
    print("Sorting trial: Nearly sorted type 2")
    print("  (few items out of order)")

    # Make dataset
    print("Creating dataset ... ", end="", flush=True)
    data = [ i * MAX_VAL // BIG_SIZE for i in range(BIG_SIZE) ]
    if BIG_SIZE >= 2:
        data[0], data[BIG_SIZE-1] = data[BIG_SIZE-1], data[0]
    assert len(data) == BIG_SIZE
    for val in data:
        assert 0 <= val <= MAX_VAL
    print("DONE")
    print(f"Size = {len(data):,}")
    print()

    # Sort
    do_sort(data)


def try_sort_messy():
    """Call do_sort on "messy" data.
    Size is BIG_SIZE (global). Values in [0, MAX_VAL (global)].
    """

    # Initial message
    print("Sorting trial: Random-ish data")

    # Make dataset
    print("Creating dataset ... ", end="", flush=True)
    data = list(range(BIG_SIZE))  # Only size of this list matters
    phi = 1.6180339887498948482
    for i in range(BIG_SIZE):
        x = (i+1)*phi
        fracpart = x - int(x)
        data[i] = int(fracpart * (1+MAX_VAL))
    assert len(data) == BIG_SIZE
    for val in data:
        assert 0 <= val <= MAX_VAL
    print("DONE")
    print(f"Size = {len(data):,}")
    print()

    # Sort
    do_sort(data)


def iter_str(the_iterable, max_chars):
    """Return str form of iterable, length limited to max_chars.
    Returned string ends with "..." if not all values will fit.
    As a last resort, returns "-".
    max_chars must be a positive int.

    >>> iter_str([1,2,3], 11)
    '[1, 2, 3]'
    >>> iter_str([1,2,3,4], 11)
    '[1, 2, ...'
    >>> iter_str([1234567], 6)
    '[ ...'
    >>> iter_str([1234567], 3)
    '-'
    """

    assert isinstance(max_chars, int)
    assert max_chars > 0

    # --- BEGIN Configuration ---

    open_str = "["    # Opening for str of iterable
    close_str = "]"   # Closing for str of iterable
    sep_str = ", "    # Separator for iterable items
    ellipses = "..."

    end_incomplete = ellipses
        # Ending for incomplete listing of items.
    short_str = open_str + " " + ellipses
        # Short representation, for when no items fit in string.

    # --- END Configuration ---

    if len(short_str) > max_chars:
        short_str = "-"

    last_good_pos = None
        # Good pos: place we can put end_incomplete without exceeding
        #  max_chars.

    output = open_str  # Our output string
    first = True  # First loop iteration?
    # Construct string until done or we run out of characters.
    for val in the_iterable:
        if first:
            first = False
        else:
            output += sep_str
            pos = len(output)
            if pos + len(end_incomplete) <= max_chars:
                last_good_pos = pos
        output += repr(val)
        if len(output) > max_chars:
            break
    else:
        output += close_str
        if len(output) <= max_chars:  # All is well? Return full string.
            return output

    # No iterable items fit? Then return a short string.
    if last_good_pos is None:
        assert len(short_str) <= max_chars
        return short_str

    # Return a string with ellipses at the end.
    assert isinstance(last_good_pos, int)
    output = output[0:last_good_pos] + end_incomplete
    assert len(output) <= max_chars
    return output


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
# Sorts a number of datasets, printing results.

if __name__ == "__main__":

    # ********** Dataset spec's **********

    print(f"Size of large datasets: {BIG_SIZE:,}")
    print("(To change this, set BIG_SIZE in the source code.)")
    print(f"Values in datasets range from 0 to {MAX_VAL:,}")

    # ********** Sorting **********

    print()
    try_sort_small()

    # MESSY-DATA TRIAL MOVED BEFORE NEARLY-SORTED DATA TRIALS
    print()
    try_sort_messy()

    print()
    try_sort_nearly_sorted1()

    print()
    try_sort_nearly_sorted2()

    # ********** Done **********

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

