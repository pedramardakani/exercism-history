"""Simulate Bob the lackadaisical teenager."""


def response(hey_bob: str) -> str:
    """Respond based on the tone of the received message.

    :param hey_bob: str - prompt.
    :return: str - Bob's answer."""
    parsed = hey_bob.rstrip()
    if parsed == '':
        return "Fine. Be that way!"
    is_yelling = parsed.isupper()
    is_question = parsed.endswith('?')
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."
