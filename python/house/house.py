"""Exercism's House Challenge."""

verses = (
    "This is",
    "the house that Jack built.",
    "the malt that lay in",
    "the rat that ate",
    "the cat that killed",
    "the dog that worried",
    "the cow with the crumpled horn that tossed",
    "the maiden all forlorn that milked",
    "the man all tattered and torn that kissed",
    "the priest all shaven and shorn that married",
    "the rooster that crowed in the morn that woke",
    "the farmer sowing his corn that kept",
    "the horse and the hound and the horn that belonged to",
)


def gen_verse(index: int):
    return f"{verses[0]} {' '.join([verses[i] for i in range(index, 0, -1)])}"


def recite(start_verse: int, end_verse: int) -> list[str]:
    return [gen_verse(i) for i in range(start_verse, end_verse+1)]
