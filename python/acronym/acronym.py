"""Exercism's Acronym Challenge."""

import re


def abbreviate(words: str) -> str:
    cleaned = re.sub(r'[^a-zA-Z\-\s]', "", words)
    parsed = re.split(r'\W', cleaned)
    return ''.join((word[0].upper() for word in parsed if word))
