"""The Extract parto of ETL challenge (Extract-Transform-Load) on the Exercism website."""

import itertools


def transform(legacy_data: dict[int, str]) -> dict[str, int]:
    parsed_data = dict()
    for score, letters in legacy_data.items():
        lowered = map(lambda letter: letter.lower(), letters)
        parsed_data.update(dict(itertools.zip_longest(lowered, [],
                                                      fillvalue=score)))
    return parsed_data
