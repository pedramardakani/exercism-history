"""Exercism's Pig Latin Challenge."""

import re

RE_CONSONANT = re.compile(r'[aieou]|y(?=t)|x(?=r)')
RE_VOWELGROUP = re.compile(r'thr|th|ch|sh|sch|qu|rh|[^aieou]')


def pigify(word: str) -> str:
    """Pig-latin only a single word."""
    # Check for consonants first
    if RE_CONSONANT.match(word):
        return word + "ay"
    # Get the length of the vowel group
    check = RE_VOWELGROUP.match(word)
    if word[check.end():].startswith("qu"):
        return word[check.end()+2:] + word[:check.end()+2] + "ay"
    return word[check.end():] + word[:check.end()] + "ay"


def translate(text: str) -> str:
    """Pig-latin an entire text."""
    return ' '.join(map(pigify, text.split()))
