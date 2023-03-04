"""Exercism's isogram challenge.

An isogram (also known as a "non-pattern word") is a word or phrase without 
a repeating letter, however spaces and hyphens are allowed to appear multiple times.
"""


def is_isogram(text: str) -> bool:
    """Determine if a word or phrase is an isogram.

    :param text: str - given text.
    :return: bool - check if is isogram."""
    parsed = text.replace(' ', '').replace('-', '').lower()
    return len(parsed) == len(set(parsed))
