"""Exercism's Collatz Conjecture Challenge."""


def steps(number: int) -> int:
    """ Return the number of steps it takes to reach 1 from any given positive
    integer based on the Collatz cojecture.

    :param number: int - any positive integer.
    :return: int - steps to reach 1.
    """
    if type(number) is not int or number <= 0:
        raise ValueError("Only positive integers are allowed")
    count = 0
    num = number
    while num != 1:
        count += 1
        num = 0.5 * num if num % 2 == 0 else 3 * num + 1
    return count
