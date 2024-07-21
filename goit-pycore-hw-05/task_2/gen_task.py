import re
from collections.abc import Generator
from typing import Callable


def generator_numbers(text: str) -> Generator[float, None, None]:

    # Regular expression to find valid numbers in the text
    pattern = r"\b\d+\.\d+\b"
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]):
    # Calculates the total profit
    # by summing up all the numbers yielded by the generator function.
    total_sum = sum(func(text))
    return total_sum
