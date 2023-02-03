"""The leap year module."""


def leap_year(year: int) -> bool:
    """Given a year, report if it is a leap year.

    :param year: int - the queried year.
    :return: bool - if it is a leap year or not."""
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0
