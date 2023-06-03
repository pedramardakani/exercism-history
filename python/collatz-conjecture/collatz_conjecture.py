"""Exercism's Collatz Conjecture Challenge."""


def generate_collatz_series(number: int) -> int:
    """Yield the steps of iteration in Collatz Conjecture"""
    num = number
    while num != 1:
        num = 0.5 * num if num % 2 == 0 else 3 * num + 1
        yield num


def steps(number: int) -> int:
    """ Return the number of steps it takes to reach 1 from any given positive
    integer based on the Collatz cojecture.

    :param number: int - any positive integer.
    :return: int - steps to reach 1.
    """
    if type(number) is not int or number <= 0:
        raise ValueError("Only positive integers are allowed")
    return len(tuple(generate_collatz_series(number)))
