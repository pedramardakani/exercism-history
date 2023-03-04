"""Exercism's isogram challenge.

An isogram (also known as a "non-pattern word") is a word or phrase without 
a repeating letter, however spaces and hyphens are allowed to appear multiple times.
"""

import string


def is_isogram(text: str) -> bool:
    """Determine if a word or phrase is an isogram.

    :param text: str - given text.
    :return: bool - check if is isogram."""
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter in string.ascii_lowercase and lowered_text.count(letter) > 1:
            return False
    return True
