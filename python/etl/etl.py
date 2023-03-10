"""The Extract parto of ETL challenge (Extract-Transform-Load) on the Exercism website."""


def transform(legacy_data: dict[int, str]) -> dict[str, int]:
    return {
        letter.lower(): score
        for score in legacy_data
        for letter in legacy_data[score]
    }
