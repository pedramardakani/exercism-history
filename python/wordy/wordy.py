"""Exercism's Wordy Challenge."""

OPS = {
    "plus": "__add__",
    "minus": "__sub__",
    "multiplied by": "__mul__",
    "divided by": "__truediv__",
}


def isnumber(duck: str) -> bool:
    """Digits preceded by a plus or minus sign are valid numbers."""
    return duck.removeprefix("-").removeprefix("+").isdigit()


def answer(question: str) -> int | float:
    # Check for a valid question
    if not question.startswith("What is"):
        raise ValueError("unknown operation")
    # Clean up and parse the expression
    expression = question.removeprefix("What is").removesuffix("?")
    if not expression:
        raise ValueError("syntax error")
    # Replace the words with the actual mathematical operation
    for name, dunder in OPS.items():
        expression = expression.replace(name, dunder)
    print(expression)
    # The replaced operators must not have whitespace
    iterator = iter(expression.split())
    # Force evaluation from left to right. "lhs" stands for "left-hand-side"
    # and "rhs" for " right-hand-side".
    lhs = next(iterator)
    while True:
        # Check for next operator
        try:
            operator = next(iterator)
        except StopIteration:
            break
        if isnumber(operator):
            raise ValueError("syntax error")
        if operator not in OPS.values():
            raise ValueError("unknown operation")
        # Check for next operand
        try:
            rhs = next(iterator)
        except StopIteration:
            raise ValueError("syntax error")
        # Check for valid operand which might be negative or positive
        if not isnumber(rhs):
            raise ValueError("syntax error")
        # Evaluate the expression so far
        lhs = int(lhs).__getattribute__(operator)(int(rhs))
    return int(lhs)
