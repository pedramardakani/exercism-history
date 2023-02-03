"""The leap year module."""


def leap_year(year: int) -> bool:
    """Given a year, report if it is a leap year.

    :param year: int - the queried year.
    :return: bool - if it is a leap year or not."""
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False
