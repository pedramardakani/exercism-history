"""Simulate Bob the lackadaisical teenager."""

import string


def response(hey_bob: str) -> str:
    """Respond based on the tone of the received message.

    :param hey_bob: str - prompt.
    :return: str - Bob's answer."""
    parsed = hey_bob.strip()
    if parsed == '':
        return "Fine. Be that way!"

    is_question = parsed.endswith('?')
    has_letters = any(letter in string.ascii_letters for letter in parsed)
    is_yelling = has_letters and parsed.upper() == parsed
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."
