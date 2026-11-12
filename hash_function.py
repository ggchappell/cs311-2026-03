#!/usr/bin/env python3
# hash_function.py
# Glenn G. Chappell
# 2026-11-12
"""Demo of a typical hash function for integers.
For CS 311 Fall 2026
Hashing code is based on MurmurHash3 by Austin Appleby 2008.
"""

def hash_func(key):
    """Integer hash function. Takes & returns 32-bit values.

    This is a condensed Python3 rewrite of function MurmurHash3_x86_32
    from file MurmurHash3.cpp in the repository below (credit: Austin
    Appleby 2008, public domain). The input data is 4 bytes long. A
    default value used for the salt (parameter "seed" in the original
    code).

    Repository:
      http://github.com/aappleby/smhasher
    """

    assert isinstance(key, int)
    mask32 = 2**32-1  # For keeping values in 32-bit range
    assert key & mask32 == key

    salt = 0xdeadbeef  # Value chosen by GGC
    h = (key * 0xcc9e2d51) & mask32
    h = ((h << 15) & mask32) | (h >> 17)
    h = (h * 0x1b873593) & mask32
    h ^= salt
    h = ((h << 13) & mask32) | (h >> 19);
    h = ((h * 5) + 0xe6546b64) & mask32
    h ^= 4 ^ (h >> 16);
    h = (h * 0x85ebca6b) & mask32
    h ^= h >> 13;
    h = (h * 0xc2b2ae35) & mask32
    return h ^ (h >> 16)


# Main program
# Repeatedly input a 32-bit integer, hash it using function hash_func,
# and print the integer and its hash in both decimal and binary.
if __name__ == "__main__":
    mask32 = 2**32-1  # For keeping values in 32-bit range
    print()
    print("Hash Function Demo")
    print()
    while True:
        try:
            line = input("Type a 32-bit integer (blank line to quit): ")
            line = line.strip()
            if line == "":
                print()
                break
            inval = int(line) & mask32
        except:
            print()
            print(f"*** Please type an integer.")
            print()
        else:
            # Apply hash function
            print()
            print("Hashing")
            outval = hash_func(inval);

            # Print values in decimal & binary
            print(f"Decimal: {inval:,} -> {outval:,}")
            print(f"Binary:  {inval:032b} -> {outval:032b}")
            print()

