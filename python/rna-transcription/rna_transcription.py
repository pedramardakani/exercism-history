"""Exercism's RNA Transcription challenge."""

translation_table = str.maketrans("T", "A")
translation_table.update(str.maketrans("G", "C"))
translation_table.update(str.maketrans("A", "U"))
translation_table.update(str.maketrans("C", "G"))


def to_rna(dna_strand: str):
    """Given a DNA strand, return its RNA complement (per RNA transcription).

    :param dna_strand: str - a strand of dna.
    :return: str - the corresponding rna."""
    return dna_strand.translate(translation_table)
