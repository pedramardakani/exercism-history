"""Exercism's rotational cypher challenge (aka Caesar Cypher)"""

import string

MAX_UPPERCASE = ord('Z')
MIN_UPPERCASE = ord('A')
MAX_LOWERCASE = ord('z')
MIN_LOWERCASE = ord('a')


def rotate(text: str, key: int) -> str:
    initial = list(text)

    def helper(i: str) -> str:
        if i not in string.ascii_letters:
            return i
        rotated = ord(i) + key
        if i.isupper() and rotated > MAX_UPPERCASE:
            rotated -= MAX_UPPERCASE - MIN_UPPERCASE + 1
        if i.islower() and rotated > MAX_LOWERCASE:
            rotated -= MAX_LOWERCASE - MIN_LOWERCASE + 1
        return chr(rotated)

    return ''.join(list(map(helper, initial)))
