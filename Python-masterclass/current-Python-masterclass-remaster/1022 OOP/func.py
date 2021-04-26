from typing import List
import unittest


# a = [1, 2, 3, 4, 5]
# b = [1, 3, 6, 10, 15]


def list_sum(numbers: List[float]) -> list[float]:
    result = []
    total = 0
    for num in numbers:
        total += num
        result.append(total)

    return result


def division(num1, num2):
    assert num2 != 0, "You can't divide by 0"
    return num1 // num2
























