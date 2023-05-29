"""Exercism's ISBN Verifier challenge."""


def is_valid(isbn: str) -> bool:
    """Return True if the given ISBN-10 string is valid.

    :param isbn: str - given ISBN-10 string, may be hyphenated.
    :return: bool - True if ISBN-10 is valid, False otherwise."""
    parsed = list(isbn.replace("-", ""))
    # ISBN must be 10 digits
    if len(parsed) != 10:
        return False
    # Validate the check digit
    if parsed[-1].lower() == "x":
        parsed[-1] = "10"
    # Discard ISBN if contains non-digits
    if not all((char.isdigit() for char in parsed)):
        return False
    # Calculate by the ISBN verification formula
    total = sum((int(digit) * (10 - index)
                for index, digit in enumerate(parsed)))
    return total % 11 == 0
