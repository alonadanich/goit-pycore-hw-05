import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r"-?\d+\.\d+|-?\d+"
    for match in re.finditer(pattern, text):
        yield float(match.group())
def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1500.55 як основний дохід, доповнений додатковими надходженнями 134.34 і 673.00 доларів. "
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income: .2f}")