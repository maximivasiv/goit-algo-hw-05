import re
from typing import Callable


def generator_numbers(text: str):
    # шукаємо дійсні числа
    pattern = r"\b\d+\.\d+\b"

    matches = re.findall(pattern, text)

    for number in matches:
        yield float(number)

def sum_profit(text: str, func: Callable):
    total = 0
    for number in func(text):
        total += number
    return total
