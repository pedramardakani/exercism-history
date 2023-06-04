"""Exercism's Triangle Challenge."""


def istriangle(sides: list[int | float]) -> bool:
    if len(sides) != 3 or not all(sides):
        return False
    sorted_sides = sorted(sides)
    return sum(sorted_sides[:2]) >= sorted_sides[2]


def equilateral(sides: list[int | float]) -> bool:
    if istriangle(sides) and len(set(sides)) == 1:
        return True
    return False


def isosceles(sides: list[int | float]) -> bool:
    if istriangle(sides) and len(set(sides)) < 3:
        return True
    return False


def scalene(sides: list[int | float]) -> bool:
    if istriangle(sides) and len(set(sides)) == 3:
        return True
    return False
