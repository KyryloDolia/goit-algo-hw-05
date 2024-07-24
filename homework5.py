import re
from typing import Callable


# Перше завдання
def caching_fibonacci() -> Callable[[int], int]:

    cache = {}
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci



# Друге завдання
def generator_numbers(text: str):
    pattern = r"[+-]?\d*\.\d+|\d+\.\d*|\d+"
    matches = re.findall(pattern, text)
    for i in matches:
        yield float(i)
    

def sum_profit(text: str, func: Callable):
    return sum(func(text))
