
def calcFunc(value_1: int, value_2: int, operator: str) -> float:
    """Calculator function to feed /services/calculator endpoint."""

    if operator == 'sum':
        result = value_1 + value_2

    elif operator == 'sub':
        result = value_1 - value_2

    elif operator == 'mul':
        result = value_1 * value_2

    elif operator == 'div':
        result = value_1 / value_2

    return result
