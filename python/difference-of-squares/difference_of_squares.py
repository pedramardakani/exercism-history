"""
Find the difference between the square of the sum and the sum of the squares of 
the first N natural numbers.
"""


def square_of_sum(number: int) -> int:
    """Add all natural numbers until the input and return the square.

    :param number: int - final number.
    :return: int - square of sum of all numbers."""

    return ((number + 1) * number / 2) ** 2


def sum_of_squares(number: int) -> int:
    """Raise all natural numbers until the input up to power of two and return sum.

    :param number: int - final number.
    :return: int - sum of all squares of numbers."""

    return number * (number + 1) * (2 * number + 1) / 6


def difference_of_squares(number: int) -> int:
    """Return the difference between square of sum and sum of squares.

    :param number: int - the final number.
    :return: int - the difference."""

    return square_of_sum(number) - sum_of_squares(number)
