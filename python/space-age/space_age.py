"""Exercism's Space Age Challenge"""


class SpaceAge:
    """Given age in seconds, calculate age on other planets."""
    # In seconds
    EARTH_YEAR = 365.25 * 24 * 60 * 60

    # Each orbital period is equals to XXX earth years
    ORBITAL_PER_EARTH_YEAR = {
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

    def calculate_age(self, coefficient: float) -> float:
        return round(self.seconds / (coefficient * self.EARTH_YEAR), 2)

    # Decorates functions following the "on_XXX" pattern
    def planet(func):
        def wrapper(self):
            name = func.__name__.removeprefix("on_").upper()
            return self.calculate_age(self.ORBITAL_PER_EARTH_YEAR[name])
        return wrapper

    @planet
    def on_mercury(self) -> float:
        pass

    @planet
    def on_venus(self) -> float:
        pass

    @planet
    def on_earth(self) -> float:
        pass

    @planet
    def on_mars(self) -> float:
        pass

    @planet
    def on_jupiter(self) -> float:
        pass

    @planet
    def on_saturn(self) -> float:
        pass

    @planet
    def on_uranus(self) -> float:
        pass

    @planet
    def on_neptune(self) -> float:
        pass
