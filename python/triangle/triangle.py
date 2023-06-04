"""Exercism's Triangle Challenge."""

from typing import Callable

side_t = list[int | float]


def istriangle(sides: side_t) -> bool:
    return (len(sides) == 3
            and all((s > 0 for s in sides))
            and sum(sides) >= 2 * max(sides))


def check_triangle(func: Callable) -> Callable | False:
    """A decorator that checks for triangles."""
    def wrapper(*args):
        return istriangle(*args) and func(*args)
    return wrapper


@check_triangle
def equilateral(sides: side_t) -> bool:
    return len(set(sides)) == 1


@check_triangle
def isosceles(sides: side_t) -> bool:
    return len(set(sides)) < 3


@check_triangle
def scalene(sides: side_t) -> bool:
    return len(set(sides)) == 3
