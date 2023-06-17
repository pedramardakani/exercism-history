"""Exercism's List-ops challenge."""

import typing


def append(items_1: list, items_2: list) -> list:
    return [*items_1, *items_2]


def _concat_helper(lists: list) -> typing.Any:
    for item in lists:
        yield from item


def concat(lists: list) -> list:
    return list(_concat_helper(lists))


def filter(function: typing.Callable, items: list) -> list:
    return [item for item in items if function(item)]


def length(items: list) -> int:
    return len(items)


def map(function: typing.Callable, items: list) -> list:
    return [function(item) for item in items]


def foldl(function: typing.Callable, items: list, initial: int | float) -> int | float:
    result = initial
    for item in items:
        result = function(result, item)
    return result


def foldr(function: typing.Callable, items: list, initial: int | float) -> int | float:
    return foldl(function, reversed(items), initial)


def reverse(items) -> list:
    return items[::-1]
