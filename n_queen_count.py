#!/usr/bin/env python3
# n_queen_count.py
# Glenn G. Chappell
# 2026-09-23
"""Print solutions to the n-Queens problem.
Example of Recursive Backtracking
Based on n_queen.py
For CS 311 Fall 2026
"""

# We represent a partial queen placement on a chessboard using a list
# (board) and an int (n). The int (n) gives the size of the chessboard.
# Thus, n = 8 means an 8 x 8 chessboard. List board is a listing of the
# queen positions (columns) on 0 or more rows of the chessboard (at most
# n rows). There is at most one queen per row. Its position (column) is
# given by a number from 0 to n-1, inclusive.
#
# For example, board == [1, 3] with n = 4 means a 4 x 4 chessboard with
# queens in its first 2 rows. The queen in the row 0 (1st row) lies in
# column 1 (the 2nd square), and the queen in row 1 (2nd row) lies in
# column 3 (the 4th & last square). This is pictured below:
#
# +---+---+---+---+
# |   | Q |   |   |
# +---+---+---+---+
# |   |   |   | Q |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
#
# We print a queen arrangement by printing the position of the queen in
# each column. For example, "1 3 0 2" represents the following
# arrangement of queens on a 4x4 chessboard:
#
# +---+---+---+---+
# |   | Q |   |   |
# +---+---+---+---+
# |   |   |   | Q |
# +---+---+---+---+
# | Q |   |   |   |
# +---+---+---+---+
# |   |   | Q |   |
# +---+---+---+---+


# check_queen
# Given a partial solution to the n-Queens Problem (see above),
# determine whether a proposed new queen placement on the next row is
# acceptable, that is, if it cannot attack any any of the existing
# queens. If there is no possible attack, then the return value is
# true.
def check_queen(board, n, newcol):
    assert isinstance(n, int)
    assert n > 0
    assert isinstance(board, list)
    assert len(board) <= n
    #for x in board:
    #    assert isinstance(x, int)
    #    assert 0 <= x < n
    # board must represent a nonattacking placement of queens.

    newrow = len(board)

    # Iterate through existing queens
    for oldrow in range(newrow):
        oldcol = board[oldrow]

        # Existing queen: oldrow, oldcol
        # Proposed new queen: newrow, newcol
        # Determine whether new queen can attack old queen

        # Vertical attack (same column)?
        if newcol == oldcol:
            return False

        # Diagonal attack
        if newrow-oldrow == abs(newcol-oldcol):
            return False

        # NOTE. We do not need to check for horizontal attack (same
        #  row) because of the assumption that there is at most one
        #  queen in each row.

    return True


# n_queen_count_recurse
# Given a partial solution to the n-Queens Problem (see above), return
# number of non-attacking placements of n queens that include the given
# queens.
def n_queen_count_recurse(board, n):
    assert isinstance(n, int)
    assert n > 0
    assert isinstance(board, list)
    assert len(board) <= n
    #for x in board:
    #    assert isinstance(x, int)
    #    assert 0 <= x < n
    # board must represent a nonattacking placement of queens.

    # BASE CASE

    if len(board) == n:
        # A full solution! It counts as 1; return that.
        return 1

    # RECURSIVE CASE

    total = 0

    # Try each position in next row
    for newcol in range(n):
        # If we can add a queen in position newcol in the next row ...
        if check_queen(board, n, newcol):
            # ... then do it, and recurse.
            board.append(newcol)       # Add new queen
            total += n_queen_count_recurse(board, n)
                                       # Recursive call
            board.pop();               # Remove new queen

    return total


# n_queen
# Count all solutions to the n-Queens Problem (see above) for a
# chessboard of the given size.
def n_queen_count(n):
    assert isinstance(n, int)
    assert n > 0

    board = []  # Empty board
    return n_queen_count_recurse(board, n)


# Main program
# Repeatedly input an integer n and count n-Queen solutions.
# Terminates on fatal error in input or empty input.
# Retries if input is not integer or n <= 0
if __name__ == "__main__":
    while True:
        print()
        print("n-Queen Counter")
        print()
        try:
            line = input("Chessboard size (blank line to quit)? ")
            if line == "":
                print()
                break
            n = int(line)
            if n <= 0: raise Exception()
        except:
            print()
            print("Please type a positive integer")
        else:
            print()
            print(f"Number of n-Queen Solutions", end="")
            print(" for {n} x {n} chessboard: ")
            print(f"  {n_queen_count(n)}")

