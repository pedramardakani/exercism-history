"""The leap year module."""


def leap_year(year: int) -> bool:
    """Given a year, report if it is a leap year.

    :param year: int - the queried year.
    :return: bool - if it is a leap year or not."""
    match year:
        # The order of the following cases are part of the logic! Please do not change
        # the ordering without running unit-tests.
        case y if y % 400 == 0:
            # If year is divisable by 400 it already is divisable by 100, so we
            # do not need to check for it explicitely.
            return True
        case y if y % 100 == 0:
            return False
        case y if y % 4 == 0:
            return True
        case _:
            return False
