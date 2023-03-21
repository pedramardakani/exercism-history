"""Exercism's sum of multiples challenge."""


def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    return sum({multiple for factor in multiples if factor for multiple in range(factor, limit, factor)})
