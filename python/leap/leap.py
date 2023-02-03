"""The leap year module."""


def leap_year(year: int) -> bool:
    """Given a year, report if it is a leap year.

    :param year: int - the queried year.
    :return: bool - if it is a leap year or not."""
    match year:
        case y if y % 100 == 0 and y % 400 == 0:
            return True
        case y if y % 100 == 0:
            return False
        case y if y % 4 == 0:
            return True
        case _:
            return False
