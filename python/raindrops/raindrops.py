"""The raindrops challenge on the exercism website."""

factor_sound = {
    3: "Pling",
    5: "Plang",
    7: "Plong",
}


def convert(number: int) -> str:
    """Produce raindrop sounds based on factors.

    :param number: int - the input number.
    :return: str - added sounds or the number itself."""
    sounds = (sound for factor, sound in factor_sound.items()
              if number % factor == 0)
    result = "".join(sounds)
    if result:
        return result
    return str(number)
