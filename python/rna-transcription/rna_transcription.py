"""Exercism's RNA Transcription challenge."""

dna_to_rna_table = str.maketrans("TGAC", "ACUG")


def to_rna(dna_strand: str):
    """Given a DNA strand, return its RNA complement (per RNA transcription).

    :param dna_strand: str - a strand of dna.
    :return: str - the corresponding rna."""
    return dna_strand.translate(dna_to_rna_table)
