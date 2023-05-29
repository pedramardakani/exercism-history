import datetime as dt


def add(moment: dt.datetime) -> dt.datetime:
    """Add 10**9 seconds to the 'moment' given.

    :param moment: datetime.datetime - initial moment.
    :return: datetime.datetime - moment after a gigasecond.
    """
    return moment + dt.timedelta(seconds=10**9)
