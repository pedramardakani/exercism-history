"""Functions which helps the locomotive engineer to keep track of the train."""

WagonList = list[int, ...]


def get_list_of_wagons(*ids: int) -> WagonList:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(ids)


def fix_list_of_wagons(each_wagons_id: WagonList,
                       missing_wagons: WagonList) -> WagonList:
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    wagon_1, wagon_2, loco_id, *rest = each_wagons_id
    return [loco_id, *missing_wagons, *rest, wagon_1, wagon_2]


def add_missing_stops(routing: dict, **stops: dict) -> dict:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return {**routing, "stops": list(stops.values())}


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
