MAX_SQUARES = 64

def square(number: int) -> int:
    """Return number of grains on a square of a chessboard.
    
    :param number: int - square to check number of grains on it.
    :return: int - number of grains on this square."""
    if 1 <= number <= MAX_SQUARES:
        return 2 ** (number - 1)
    raise ValueError(f"square must be between 1 and {MAX_SQUARES}")


def total() -> int:
    """Return total number of grains on the chessboard.

    Since the problem is a geometrical series, we can follow the mathematic definitions
    to easily derive the total number of grains on the board instantly. More here:
    https://en.wikipedia.org/wiki/1_%2B_2_%2B_4_%2B_8_%2B_%E2%8B%AF
    
    :return: int - total number of grains on the chessboard."""
    return (2 ** MAX_SQUARES) - 1
