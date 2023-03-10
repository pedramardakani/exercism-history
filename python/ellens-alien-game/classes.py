"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
Point = typing.NamedTuple(
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created: int = 0

    def __init__(self, x_coordinate: float, y_coordinate: float):
        # Effects on class
        Alien.total_aliens_created += 1

        # Effects on the object itself
        self.health = 3
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def hit(self) -> None:
        if self.health > 0:
            self.health -= 1

    def is_alive(self) -> bool:
        return self.health > 0

    def teleport(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, some_argument):
        pass


def new_aliens_collection(start_positions: list[tuple[float, float]]) -> list[Alien]:
    return [Alien(x_coords, y_coords) for x_coords, y_coords in start_positions]
