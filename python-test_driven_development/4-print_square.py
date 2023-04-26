#!/usr/bin/python3
"""" This module print the square """


def print_square(size):
    """" Printing the square """
    if not isinstance(size, (int,)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
