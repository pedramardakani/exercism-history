"""Exercism's flatten array challenge."""


def _flatten_helper(items: list | tuple):
    for item in items:
        try:
            iterator = iter(item)
        except TypeError as err:
            if item is not None:
                yield item
        else:
            # If the delegated generator returns None, the __next__ method
            # is called on it automatically. So no "None"s returned. More on
            # https://peps.python.org/pep-0380/
            yield from _flatten_helper(iterator)


def flatten(items: list[int | float | str | None | list[...]]) -> list[int | float | str]:
    """Take a nested list and return a single flattened list with all values except nil/null."""
    return list(_flatten_helper(items))
