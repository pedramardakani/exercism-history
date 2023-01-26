"""Functions to prevent a nuclear meltdown."""

from enum import Enum
from typing import Union

num_type = Union[int, float]


class EfficiencyBands(Enum):
    """Bands used to show the efficiency level."""
    ONE = 'green'
    TWO = 'orange'
    THREE = 'red'
    FOUR = 'black'


def is_criticality_balanced(temperature: num_type,
                            neutrons_emitted: num_type) -> bool:
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    if temperature >= 800:
        return False
    if neutrons_emitted <= 500:
        return False
    if temperature * neutrons_emitted >= 500000:
        return False
    return True


def generated_power(voltage: num_type, current: num_type) -> num_type:
    """Calculate generated power.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :return: int or float - generated power.
    """
    return voltage * current


def reactor_efficiency(voltage: num_type, current: num_type, theoretical_max_power: num_type) -> str:
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    efficiency = 100 * \
        generated_power(voltage, current) / theoretical_max_power

    if efficiency >= 80:
        band = EfficiencyBands.ONE
    elif efficiency >= 60:
        band = EfficiencyBands.TWO
    elif efficiency >= 30:
        band = EfficiencyBands.THREE
    else:
        band = EfficiencyBands.FOUR
    return band.value


def isLow(status: num_type, threshold: num_type) -> bool:
    """Check if is in fail-safe 'low' condition.

    :param status: int or float - current status to be compared with the threshold.
    :param threshold: int or float - current threshold.
    :return: bool - if status should be considered low or not."""
    return status < 0.9 * threshold


def isNormal(status: num_type, threshold: num_type) -> bool:
    """Check if is in fail-safe 'normal' condition.

    :param status: int or float - current status to be compared with the threshold.
    :param threshold: int or float - current threshold.
    :return: bool - if status should be considered normal or not."""
    return (status <= 1.1 * threshold) and (status >= 0.9 * threshold)


def fail_safe(temperature: num_type,
              neutrons_produced_per_second: num_type,
              threshold: num_type) -> str:
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER')."""
    status = temperature * neutrons_produced_per_second

    if isLow(status, threshold):
        return 'LOW'
    if isNormal(status, threshold):
        return 'NORMAL'
    return 'DANGER'
