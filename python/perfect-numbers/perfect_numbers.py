def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    divisors = (div for div in range(1, number//2 + 1) if number % div == 0)
    match sum(divisors):
        case s if s > number:
            return "abundant"
        case s if s < number:
            return "deficient"
        case s if s == number:
            return "perfect"
