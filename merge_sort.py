#!/usr/bin/env python3
# merge_sort.py
# Glenn G. Chappell
# Started: 2026-09-29
# Updated: 2026-09-30
"""Sorting Demo: Merge Sort (recursive).
For CS 311 Fall 2026
"""


# Size of large datasets
BIG_SIZE = 3_000_000

# Values in datasets range from 0 to MAX_VAL
MAX_VAL = 999_999_999


def merge_sort(container, index1=None, index2=None):
    """Do Merge Sort on given range.
    Range to be sorted is [container[index1], container[index2]),
    or the whole container if index1, index2 are not passed.

    Uses stable_merge.

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

    # Compute size of range
    size = index2 - index1

    # BASE CASE

    if size <= 1:
        return

    # RECURSIVE CASE

    # Create iterator to middle of range
    middle_index = index1 + size//2

    # Recursively sort the two lists
    merge_sort(container, index1, middle_index)
    merge_sort(container, middle_index, index2)

    # And merge them
    stable_merge(container, index1, middle_index, index2);


def stable_merge(container, begin, middle, end):
    """Do Stable Merge of 2 contiguous sorted ranges.
    Sorted ranges:
      * [container[begin], container[middle])
      * [container[middle], container[end])

    Pre:
    * Container is an indexable sequence.
    * begin, middle, end have type int.
    * begin <= middle <= end.
    * Integers in [begin, end) are valid indices for container.
    * Range [container[begin], container[middle]) is sorted
      ascending by <.
    * Range [container[middle], container[end]) is sorted
      ascending by <.
    """

    buffer = list(range(end-begin))  # Only size of this list matters
    in1 = begin
    in2 = middle
    out = 0

    # Merge two sorted lists into a single list in buff.
    while in1 != middle and in2 != end:
        if container[in2] < container[in1]:  # Do this way to be stable
            buffer[out] = container[in2]
            in2 += 1
            out += 1
        else:
            buffer[out] = container[in1]
            in1 += 1
            out += 1

    # Move remainder of original sequence to buffer.
    # Only one of the following two loops will do anything, since the
    #  other is given an empty source range.
    for i in range(in1, middle):
        buffer[out] = container[i]
        i += 1
        out += 1
    for i in range(in2, end):
        buffer[out] = container[i]
        i += 1
        out += 1
    assert out == end - begin

    # Copy back to original container
    for i, val in enumerate(buffer, start=begin):
        container[i] = val


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
    merge_sort(container)

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
    data = [ i * MAX_VAL // BIG_SIZE for i in range(BIG_SIZE) ]
    for i in range(0, BIG_SIZE-3, 2):
        data[i], data[i+3] = data[i+3], data[i]
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
    dummy = input(msg)


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

    print()
    try_sort_nearly_sorted1()

    print()
    try_sort_nearly_sorted2()

    print()
    try_sort_messy()

    # ********** Done **********

    # Wait for user
    print()
    user_pause("Press ENTER to quit ")

