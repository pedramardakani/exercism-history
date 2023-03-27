"""Exercism's anagram challenge."""


def find_anagrams(word: str, candidates: set[str]) -> set[str]:
    """Return a set containing anagrams of the word.

    :param word: str - word to check with.
    :param candidates: set[str] - the candidate set of strings being checked.
    :return: set[str] - the set of anagrams."""
    low_word = word.lower()
    criteria = sorted(low_word)
    return {cand for cand in candidates
            if (low_cand := cand.lower()) != low_word and criteria == sorted(low_cand)}
