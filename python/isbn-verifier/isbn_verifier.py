"""Exercism's ISBN Verifier challenge."""


def is_valid(isbn: str) -> bool:
    """Return True if the given ISBN-10 string is valid.

    :param isbn: str - given ISBN-10 string, may be hyphenated.
    :return: bool - True if ISBN-10 is valid, False otherwise."""
    parsed = list(isbn.replace("-", ""))
    # ISBN must be 10 digits
    if len(parsed) != 10:
        return False
    # Replace the check digit if any
    if parsed[-1].lower() == "x":
        parsed[-1] = "10"
    total = 0
    for index, digit in enumerate(parsed):
        if not digit.isdigit():
            return False
        total += int(digit) * (10 - index)
    return total % 11 == 0
