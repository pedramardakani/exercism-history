"""Two-fer or 2-fer is short for two for one."""


def two_fer(name: str = "you") -> str:
    """Given a name, return a string with the message:

        One for name, one for me.

    Where "name" is the given name. However, if the name is missing, return the string:

        One for you, one for me.

    :param name: str - the name of the person to print, with a default value of 'you'.
    :return: str - the two-fer string with the given name."""
    return f"One for {name}, one for me."
