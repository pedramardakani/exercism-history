"""Exercism's Space Age Challenge"""


class SpaceAge:
    """Given age in seconds, calculate age on other planets."""
    # In seconds
    EARTH_YEAR = 365.25 * 24 * 60 * 60

    # Each orbital period is equals to XXX earth years
    RATIO_TO_EARTH = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds: int):
        self.seconds = seconds
        # Create all the "on_PLANET_NAME" methods here
        for planet, ratio in self.RATIO_TO_EARTH.items():
            setattr(self, f"on_{planet}", self.calculate_age(ratio))

    def calculate_age(self, ratio: float) -> float:
        return lambda r=ratio: round(self.seconds / (r * self.EARTH_YEAR), 2)
