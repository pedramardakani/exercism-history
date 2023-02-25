"""Pangram checker module.

Determine if a sentence is a pangram.
"""

import string


ALPHABET = set(string.ascii_lowercase)


def is_pangram(sentence: str) -> bool:
    """Check if a given sentence contains all English letters.

    :param sentence: str - a string consisting letters `a-z` and case insensitive.
    :return: bool - return True if sentence is a pangram."""
    return ALPHABET.issubset(sentence.lower())
