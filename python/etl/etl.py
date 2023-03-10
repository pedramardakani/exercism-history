"""The Extract parto of ETL challenge (Extract-Transform-Load) on the Exercism website."""


def transform(legacy_data: dict[int, str]) -> dict[str, int]:
    """Reformat legacy data structure to the new one.

    :param legacy_data: dict[int, str] - score is the key, and letters are the values.
    :return: dict[str, int] - letters are the keys, and each has a score as value."""
    return {
        letter.lower(): score
        for score, letters in legacy_data.items()
        for letter in letters
    }
