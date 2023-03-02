"""Functions to help Azara and Rui locate pirate treasure."""

AzaraType = tuple[str, str]
RuiType = tuple[str, tuple[str, str], str]
CombinedType = tuple[str, str, str, tuple[str, str], str]


def get_coordinate(record: tuple[str, str]) -> str:
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]


def convert_coordinate(coordinate: str) -> tuple[str]:
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)


def compare_records(azara_record: AzaraType, rui_record: RuiType) -> bool:
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    return rui_record[1] == convert_coordinate(azara_record[1])


def create_record(azara_record: AzaraType, rui_record: RuiType) -> CombinedType | str:
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record):
        record = azara_record + rui_record
    else:
        record = "not a match"
    return record


def clean_up(combined_record_group: CombinedType) -> tuple[str, str, tuple[str, str], str]:
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    result = (f"('{treasure}', '{location}', {coords}, '{variant}')"
              for treasure, _, location, coords, variant in combined_record_group)
    return "\n".join(result) + "\n"
