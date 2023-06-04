"""Exercism's Triangle Challenge."""

from typing import Callable

side_t = list[int | float]


def istriangle(sides: side_t) -> bool:
    if len(sides) != 3 or not all(sides):
        return False
    ss = sorted(sides)
    return sum(ss[:2]) >= ss[2]


def check_triangle(func: Callable) -> Callable | False:
    """A decorator that checks for trianlges.

    If the given sides cannot form a triangle, return False. Let the function
    proceed otherwise.
    """
    def wrapper(*args):
        if istriangle(*args):
            return func(*args)
        return False
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
