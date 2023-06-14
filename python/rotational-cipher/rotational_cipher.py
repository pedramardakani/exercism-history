"""Exercism's rotational cypher challenge (aka Caesar Cypher)"""

import string


def rotate(text: str, key: int) -> str:
    initial = list(text)

    def helper(i: str) -> str:
        if i not in string.ascii_letters:
            return i
        new = ord(i) + key
        if i.isupper() and new > ord('Z'):
            new = new - ord('Z') + ord('A') - 1
        if i.islower() and new > ord('z'):
            new = new - ord('z') + ord('a') - 1
        return chr(new)

    return ''.join(list(map(helper, initial)))
