"""Exercism's Wordy Challenge."""


def answer(question: str) -> int | float:
    if not question.startswith("What is"):
        raise ValueError("unknown operation")
    expression = question.removeprefix("What is ").replace("?", "").replace(
        "plus", "+").replace("divided by", "/").replace("multiplied by", "*").replace("minus", "-")
    print(f"'{expression}'")
    splitted = expression.split()
    iterator = iter(splitted)
    a = next(iterator)
    if not a.removeprefix("-").removeprefix("+").isdigit():
        raise ValueError("syntax error")
    while True:
        # Check for valid operator
        try:
            operator = next(iterator)
        except StopIteration:
            break
        if operator.isdigit():
            raise ValueError("syntax error")
        if operator not in "+-*/":
            raise ValueError("unknown operation")
        # Check for valid operand
        try:
            operand = next(iterator)
        except StopIteration:
            raise ValueError("syntax error")
        if not operand.removeprefix("-").removeprefix("+").isdigit():
            raise ValueError("syntax error")
        a = eval(' '.join((str(a), operator, operand,)))
    return int(a)
