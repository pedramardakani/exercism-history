"""Exercism's Secret Handshake Challenge."""

actions = ("wink", "double blink", "close your eyes", "jump")


def commands(binary_str: str) -> list[str]:
    queue = [a for a, c in zip(actions, reversed(binary_str)) if c == "1"]
    # The first bit means "reversed"
    if binary_str[0] == "1":
        queue.reverse()
    return queue
