"""The raindrops challenge on the exercism website."""

sounds = {
    3: "Pling",
    5: "Plang",
    7: "Plong",
}


def convert(number: int) -> str:
    """Produce raindrop sounds based on factors.

    :param number: int - the input number.
    :return: str - added sounds or the number itself."""
    result = ""
    for factor, sound in sounds.items():
        if number % factor == 0:
            result += sound
    if result:
        return result
    else:
        return str(number)
