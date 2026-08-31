# fact.py
# Glenn G. Chappell
# 2026-08-24
"""First Python program: compute factorials.
For CS 311 Fall 2026
"""


def fact(n):
    """Return the factorial of n."""
    result = 1
    for i in range(1, 1+n):
        result *= i
    return result


k = 4
print(k, "factorial:", fact(k))

k = 100
print(k, "factorial:", fact(k))


