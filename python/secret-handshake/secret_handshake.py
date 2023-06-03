"""Exercism's Secret Handshake Challenge."""

actions = ("wink", "double blink", "close your eyes", "jump", "reverse")


def commands(binary_str: str) -> list[str]:
    queue = [a for a, c in zip(actions, reversed(binary_str)) if c == "1"]
    if "reverse" in queue:
        queue.remove("reverse")
        queue.reverse()
    return queue
