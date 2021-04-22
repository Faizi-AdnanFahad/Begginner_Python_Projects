def factorial(number: int) -> float:
    """
    Calculates the factorial of a given number
    :param number: Number that its factorial is requested
    :return: The calculation of that number
    """
    result = 1
    if number != 0:
        for i in range(1, number + 1):
            result *= i
    return result


for i in range(35):
    print(factorial(i))
