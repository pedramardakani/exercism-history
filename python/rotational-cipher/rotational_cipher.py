"""Exercism's rotational cypher challenge (aka Caesar Cypher)"""

MIN_UPPERCASE = ord('A')
MIN_LOWERCASE = ord('a')


def rotate_char(char: str, key: int) -> str:
    """Rotate a single character only."""
    if char.isalpha():
        offset = MIN_UPPERCASE if char.isupper() else MIN_LOWERCASE
        return chr((ord(char) + key - offset) % 26 + offset)
    return char


def rotate(text: str, key: int) -> str:
    """Rotate an entire text."""
    return ''.join((rotate_char(item, key) for item in text))
