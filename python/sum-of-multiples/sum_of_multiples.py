"""Exercism's sum of multiples challenge."""


def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    # Purge '0' from the multiples list 'if' present.
    factors = set(multiples).difference({0})
    return sum({factor * multiple for factor in factors for multiple in range(1 + limit // factor) if factor * multiple < limit})
