"""Function used for /services/calculator endpoint."""


def calculator_func(num_a: int, num_b: int, operator: str) -> int:
    """Takes two integers and returns computed value."""

    if operator == 'sum':
        result = num_a + num_b

    elif operator == 'sub':
        result = num_a - num_b

    elif operator == 'mul':
        result = num_a * num_b

    elif operator == 'div':
        result = num_a / num_b

    return result
