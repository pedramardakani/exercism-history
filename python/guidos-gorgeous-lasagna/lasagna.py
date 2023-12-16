"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME: int = 40
LAYER_PREPARATION_TIME: int = 2

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers: int) -> int:
    """Calculate preparation time where each layer takes 2 minutes.

    :param layers: int - number of layers to prepare.
    :return: int - time it takes to prepare given number of 'layers' in minutes.
    """
    return LAYER_PREPARATION_TIME * layers

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Total number of minutes we've been cooking.

    :param number_of_layers: int - the number of layers added to the lasagna.
    :param elapsed_bake_time: int - the number of minutes the lasagna
    has been baking in the oven.
    :return: int - sum of preparation time and the time the lasagna has already
    spent baking in the oven.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time
    