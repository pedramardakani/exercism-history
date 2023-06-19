"""Exercism's Acronym Challenge."""

import re


def abbreviate(words: str) -> str:
    parsed = re.sub(r"[-_]", " ", words).split()
    return ''.join((word[0].upper() for word in parsed))
