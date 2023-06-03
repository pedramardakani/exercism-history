"""Exercism's Collatz Conjecture Challenge."""


def steps(number: int):
    if type(number) is not int or number <= 0:
        raise ValueError("Only positive integers are allowed")
    count = 0
    num = number
    while num != 1:
        if num % 2 == 0:
            num *= 0.5
        else:
            num = 3 * num + 1
        count += 1
    return count
