"""Exercism's rotational cypher challenge (aka Caesar Cypher)"""

MIN_UPPERCASE = ord('A')
MIN_LOWERCASE = ord('a')


def rotate(text: str, key: int) -> str:

    def helper(i: str) -> str:
        if i.isalpha():
            offset = MIN_UPPERCASE if i.isupper() else MIN_LOWERCASE
            return chr((ord(i) + key - offset) % 26 + offset)
        return i

    return ''.join((helper(item) for item in text))
