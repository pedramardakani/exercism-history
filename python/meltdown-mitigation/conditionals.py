"""Functions to prevent a nuclear meltdown."""

from typing import Union

NumType = Union[int, float]


def is_criticality_balanced(temperature: NumType,
                            neutrons_emitted: NumType) -> bool:
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    if (temperature < 800) and (neutrons_emitted > 500) and (temperature * neutrons_emitted < 500000):
        return True
    return False


def generated_power(voltage: NumType, current: NumType) -> NumType:
    """Calculate generated power.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :return: int or float - generated power.
    """
    return voltage * current


def reactor_efficiency(voltage: NumType, current: NumType, theoretical_max_power: NumType) -> str:
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

    match efficiency:
        case e if e >= 80:
            return 'green'
        case e if e >= 60:
            return 'orange'
        case e if e >= 30:
            return 'red'
        case _:
            return 'black'


def fail_safe(temperature: NumType,
              neutrons_produced_per_second: NumType,
              threshold: NumType) -> str:
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER')."""
    status = temperature * neutrons_produced_per_second

    match [status, threshold]:
        case [s, t] if s < 0.9 * t:
            return 'LOW'
        case [s, t] if 0.9 * t <= s <= 1.1 * t:
            return 'NORMAL'
        case _:
            return 'DANGER'
