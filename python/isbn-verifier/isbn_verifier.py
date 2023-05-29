"""Exercism's ISBN Verifier challenge."""


import string


def is_valid(isbn: str) -> bool:
    """Return True if the given ISBN-10 string is valid.

    :param isbn: str - given ISBN-10 string, may be hyphenated.
    :return: bool - True if ISBN-10 is valid, False otherwise."""
    parsed = isbn.replace("-", "")
    # ISBN must be 10 digits
    if len(parsed) != 10:
        return False
    # Begin calculation by the ISBN verification formula
    total = 0
    for index, digit in enumerate(parsed[:-1]):
        if digit not in string.digits:
            return False
        total += int(digit) * (10 - index)
    check_digit = parsed[-1]
    match parsed[-1]:
        case digit if digit.lower() == "x":
            total += 10
        case digit if digit in string.digits:
            total += int(digit)
        case _:
            return False
    return total % 11 == 0
