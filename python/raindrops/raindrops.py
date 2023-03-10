"""The raindrops challenge on the exercism website."""

sounds = {
    3: "Pling",
    5: "Plang",
    7: "Plong",
}


def convert(number: int) -> int | str:
    result = ""
    for factor, sound in sounds.items():
        if number % factor == 0:
            result += sound
    if result:
        return result
    else:
        return str(number)
