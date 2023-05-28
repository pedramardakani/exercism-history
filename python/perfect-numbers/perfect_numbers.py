"""Determine if a number is perfect, abundant, or deficient.

The Greek mathematician [Nicomachus][nicomachus] devised a
classification scheme for positive integers, identifying each as
belonging uniquely to the categories of **perfect**,
**abundant**, or **deficient** based on their [aliquot
sum][aliquot-sum].  The aliquot sum is defined as the sum of the
factors of a number not including the number itself.  For
example, the aliquot sum of 15 is (1 + 3 + 5) = 9

[nicomachus]: https://en.wikipedia.org/wiki/Nicomachus
[aliquot-sum]: https://en.wikipedia.org/wiki/Aliquot_sum
"""


def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0 or type(number) is not int:
        raise ValueError("Classification is only "
                         "possible for positive integers.")
    max_range = int(number ** 0.5) + 1
    f_low = [div for div in range(1, max_range) if number % div == 0]
    f_high = map(lambda x: number/x, f_low)
    factors = set().union(f_low, f_high)
    factors.discard(number)
    match sum(factors):
        case aliquot_sum if aliquot_sum > number:
            return "abundant"
        case aliquot_sum if aliquot_sum < number:
            return "deficient"
        case _:
            return "perfect"
