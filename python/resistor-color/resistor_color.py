"""Resistor colors."""

color_list = ["black", "brown", "red", "orange", "yellow",
              "green", "blue", "violet", "grey", "white"]

color_table = {name: index for index, name in enumerate(color_list)}


def color_code(color: str) -> int:
    """Return index of the color given, or -1 if not found.

    :param color: str - color to be checked.
    :return: int - color index."""
    return color_table.get(color.lower(), -1)


def colors() -> list[str]:
    """Return all known colors.

    :return: list[str] - the list of all known colors."""
    return color_list
