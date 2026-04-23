import re
from typing import Callable


def generator_numbers(text: str):
    # число має бути обмежене пробілами
    pattern = r" \d+\.\d+ "

    matches = re.findall(pattern, text)

    for number in matches:
        yield float(number.strip())  # прибираємо пробіли


def sum_profit(text: str, func: Callable):
    total = 0
    for number in func(text):
        total += number
    return total
