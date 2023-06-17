"""Exercism's List-ops challenge."""


def append(items_1: list, items_2: list) -> list:
    return [*items_1, *items_2]


def _concat_helper(lists: list):
    for item in lists:
        yield from item


def concat(lists: list):
    return list(_concat_helper(lists))


def filter(function: callable, items: list) -> list:
    return [item for item in items if function(item)]


def length(items: list):
    return len(items)


def map(function: callable, items: list) -> list:
    return [function(item) for item in items]


def foldl(function: callable, items: list, initial: int | float) -> int | float:
    result = initial
    for item in items:
        result = function(result, item)
    return result


def foldr(function: callable, items: list, initial: int | float) -> int | float:
    return foldl(function, reversed(items), initial)


def reverse(items) -> list:
    return items[::-1]
