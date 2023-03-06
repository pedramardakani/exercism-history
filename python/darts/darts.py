"""Exercism's darts challenge.

Write a function that returns the earned points in a single toss of a Darts game.

In our particular instance of the game, the target rewards 4 different amounts of 
points, depending on where the dart lands:

- If the dart lands outside the target, player earns no points (0 points).
- If the dart lands in the outer circle of the target, player earns 1 point.
- If the dart lands in the middle circle of the target, player earns 5 points.
- If the dart lands in the inner circle of the target, player earns 10 points.

The outer circle has a radius of 10 units (this is equivalent to the total radius
for the entire target), the middle circle a radius of 5 units, and the inner circle
 a radius of 1. Of course, they are all centered at the same point (that is, 
 the circles are concentric defined by the coordinates (0, 0)."""


import math

inner_circle = 1
middle_circle = 5
outer_circle = 10


def score(x: float, y: float) -> int:
    """Return the earned points in a single toss of a Darts game.

    :param x: float - x coordinate on the board.
    :param y: float - y coordinate on the board.
    :return: int - calculated score."""
    distance = math.sqrt(x**2 + y**2)
    if distance <= inner_circle:
        return 10
    if distance <= middle_circle:
        return 5
    if distance <= outer_circle:
        return 1
    return 0
