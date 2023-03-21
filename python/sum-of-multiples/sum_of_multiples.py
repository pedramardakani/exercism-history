"""Exercism's sum of multiples challenge."""


def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    final_set = set()
    for item in multiples:
        if item == 0:
            continue
        final_set = final_set.union(
            {item * factor for factor in range(1+limit//item) if item * factor < limit})
    return sum(final_set)
