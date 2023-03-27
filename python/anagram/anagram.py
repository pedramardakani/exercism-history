"""Exercism's anagram challenge."""


def get_letter_count(word: str) -> dict[str: int]:
    """Get a dictionary indicating a case-insensitive count of each letter in a word.

    :param word: str - word to check.
    :return: dict[str: int] - dictionary with keys of letters and values of count of each letter."""
    return {letter: word.count(letter) for letter in set(word)}


def find_anagrams(word: str, candidates: set[str]) -> set[str]:
    """Return a set containing anagrams of the word.

    :param word: str - word to check with.
    :param candidates: set[str] - the candidate set of strings being checked.
    :return: set[str] - the set of anagrams."""
    lowered_word = word.lower()
    word_status = get_letter_count(lowered_word)
    return {item for item in candidates
            if (lowered_item := item.lower()) != lowered_word and word_status == get_letter_count(lowered_item)}
