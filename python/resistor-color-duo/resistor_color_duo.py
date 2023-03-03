"""Calculate resistor value by color."""

color_list = ["black", "brown", "red", "orange", "yellow",
              "green", "blue", "violet", "grey", "white"]

color_table = {name: str(index) for index, name in enumerate(color_list)}


def value(colors: list[str, str, ...]) -> int:
    """Get the first two colors of the list and return the corresponding integer.

    :param colors: list[str, str, ...] - a list of two or more strings.
    :return: int - the integer resembling the resistor value."""
    digits = (color_table.get(color) for color in colors[:2])
    return int(''.join(digits))
