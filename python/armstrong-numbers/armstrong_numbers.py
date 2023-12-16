def is_armstrong_number(number: int) -> bool:
    """Test whether the given integer is an armstrong number.
    
    :param number: int - number to test.
    :return: bool - True if the number is an armstrong number, False otherwise."""
    if type(number) != int:
        raise TypeError("input must be an integer.")
    if number < 0:
        raise ValueError("input must be a positive integer.")
    num_as_string = str(number)
    number_of_digits = len(num_as_string)
    return number == sum(int(digit) ** number_of_digits for digit in num_as_string)
