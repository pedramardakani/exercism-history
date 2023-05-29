
# In seconds
EARTH_YEAR = 365.25 * 24 * 60 * 60


class SpaceAge:
    def __init__(self, seconds: int):
        self.seconds = seconds

    def calc(self, coefficient: float) -> int:
        return round(self.seconds / (coefficient * EARTH_YEAR), 2)

    def on_mercury(self) -> int:
        return self.calc(0.2408467)

    def on_venus(self) -> int:
        return self.calc(0.61519726)

    def on_earth(self) -> int:
        return self.calc(1)

    def on_mars(self) -> int:
        return self.calc(1.8808158)

    def on_jupiter(self) -> int:
        return self.calc(11.862615)

    def on_saturn(self) -> int:
        return self.calc(29.447498)

    def on_uranus(self) -> int:
        return self.calc(84.016846)

    def on_neptune(self) -> int:
        return self.calc(164.79132)
