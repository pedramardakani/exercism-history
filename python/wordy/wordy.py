"""Exercism's Wordy Challenge."""


def answer(question: str) -> int | float:
    # Check for a valid question
    if not question.startswith("What is"):
        raise ValueError("unknown operation")
    # Clean up and parse the expression
    expression = question \
        .removesuffix("?") \
        .replace("plus", "+") \
        .replace("minus", "-") \
        .removeprefix("What is ") \
        .replace("divided by", "/") \
        .replace("multiplied by", "*")
    iterator = iter(expression.split())
    # Force evaluation from left to right
    a = next(iterator)
    if not a.removeprefix("-").removeprefix("+").isdigit():
        raise ValueError("syntax error")
    while True:
        # Check for next operator
        try:
            operator = next(iterator)
        except StopIteration:
            break
        # Check for valid operator
        if operator.isdigit():
            raise ValueError("syntax error")
        if operator not in "+-*/":
            raise ValueError("unknown operation")
        # Check for next operand
        try:
            operand = next(iterator)
        except StopIteration:
            raise ValueError("syntax error")
        # Check for valid operand which might be negative or positive
        if not operand.removeprefix("-").removeprefix("+").isdigit():
            raise ValueError("syntax error")
        # Evaluate the expression so far
        a = eval(' '.join((str(a), operator, operand,)))
    return int(a)
