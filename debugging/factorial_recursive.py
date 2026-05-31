#!/usr/bin/python3
"""
This script calculates the factorial of a number using recursion.
"""

import sys


def factorial(n):
    """
    Calculate the factorial of a number recursively.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1

    return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
