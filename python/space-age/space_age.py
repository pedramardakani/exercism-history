"""Exercism's Space Age Challenge"""


class SpaceAge:
    """Given age in seconds, calculate age on other planets."""
    # In seconds
    EARTH_YEAR = 365.25 * 24 * 60 * 60

    # Each orbital period is equals to XXX earth years
    COEFFICIENT_EARTH = {
        "MERCURY": 0.2408467,
        "VENUS": 0.61519726,
        "EARTH": 1,
        "MARS": 1.8808158,
        "JUPITER": 11.862615,
        "SATURN": 29.447498,
        "URANUS": 84.016846,
        "NEPTUNE": 164.79132,
    }

    def __init__(self, seconds: int):
        self.seconds = seconds

    def calc(self, coefficient: float) -> int:
        return round(self.seconds / (coefficient * self.EARTH_YEAR), 2)

    def on_mercury(self) -> int:
        return self.calc(self.COEFFICIENT_EARTH["MERCURY"])

    def on_venus(self) -> int:
        return self.calc(self.COEFFICIENT_EARTH["VENUS"])

    def on_earth(self) -> int:
        return self.calc(self.COEFFICIENT_EARTH["EARTH"])

    def on_mars(self) -> int:
        return self.calc(self.COEFFICIENT_EARTH["MARS"])

    def on_jupiter(self) -> int:
        return self.calc(self.COEFFICIENT_EARTH["JUPITER"])

    def on_saturn(self) -> int:
        return self.calc(self.COEFFICIENT_EARTH["SATURN"])

    def on_uranus(self) -> int:
        return self.calc(self.COEFFICIENT_EARTH["URANUS"])

    def on_neptune(self) -> int:
        return self.calc(self.COEFFICIENT_EARTH["NEPTUNE"])
