"""Exercism's "hamming" challenge.

If we compare two strands of DNA and count the differences between them we can see 
how many mistakes occurred. This is known as the "Hamming Distance"."""


def distance(strand_a: str, strand_b: str) -> int:
    """Calculate the Hamming Distance between two DNA strands."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    count = 0
    for a, b in zip(strand_a, strand_b):
        if a != b:
            count += 1
    return count
