"""Exercism's anagram challenge."""


def find_anagrams(word: str, candidates: set[str]) -> set[str]:
    """Return a set containing anagrams of the word.

    :param word: str - word to check with.
    :param candidates: set[str] - the candidate set of strings being checked.
    :return: set[str] - the set of anagrams."""
    lowered_word = word.lower()
    word_status = sorted(lowered_word)
    return {item for item in candidates
            if (lowered_item := item.lower()) != lowered_word and word_status == sorted(lowered_item)}
