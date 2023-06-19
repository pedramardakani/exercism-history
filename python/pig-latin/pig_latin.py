"""Exercism's Pig Latin Challenge."""

import re


def pigify(word: str) -> str:
    """Pig-latin only a single word."""
    if check := re.match(r'[aieou]|y(?=t)|x(?=r)', word):
        return word + "ay"
    if check := re.match(r'thr|th|ch|sh|sch|qu|rh|[^aieou]', word):
        if word[check.end():].startswith("qu"):
            return word[check.end()+2:] + word[:check.end()+2] + "ay"
        return word[check.end():] + word[:check.end()] + "ay"


def translate(text: str) -> str:
    """Pig-latin an entire text."""
    return ' '.join((pigify(word) for word in text.split()))
