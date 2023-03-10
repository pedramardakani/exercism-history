"""The Extract parto of ETL challenge (Extract-Transform-Load) on the Exercism website."""


def transform(legacy_data: dict[int, str]) -> dict[str, int]:
    parsed_data = dict()
    for score, letters in legacy_data.items():
        for letter in letters:
            parsed_data.update({letter.lower(): score})
    return parsed_data
