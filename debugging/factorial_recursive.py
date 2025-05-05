#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input integer n.

    Raises:
        RecursionError: If n is too large and exceeds Python's recursion limit.
        ValueError: If n is negative.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the first command-line argument, convert it to an integer, and compute its factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
