"""Functions which helps the locomotive engineer to keep track of the train."""

import collections

Wagons = collections.namedtuple("Wagons", ["ID", "color"])


def get_list_of_wagons(*ids: int) -> list[int, ...]:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(ids)


def fix_list_of_wagons(each_wagons_id: list[int, ...],
                       missing_wagons: list[int, ...]) -> list[int, ...]:
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    wagon_1, wagon_2, loco_id, *rest = each_wagons_id
    # Use '*XXX,' pattern to get a 'list' of unpacked items instead of a 'tuple'.
    *ordered_wagons, = loco_id, *missing_wagons, *rest, wagon_1, wagon_2
    return ordered_wagons


def add_missing_stops(routing: dict, **kwargs: dict) -> dict:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops = [city for city in kwargs.values()]
    return {**routing, "stops": stops}


def extend_route_information(route: dict, more_route_information: dict) -> dict:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows: list[list[tuple]]) -> list[list[tuple]]:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return [list(items) for items in zip(*wagons_rows)]
