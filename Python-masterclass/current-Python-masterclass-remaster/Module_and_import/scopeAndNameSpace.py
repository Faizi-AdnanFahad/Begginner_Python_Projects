
def factorial(n: int) -> float:
    """Calculate n! iteratively"""
    result = 1
    if n > 1:
        for i in range(2, n + 1):
            result *= i
    return result


def factorial_recursive(n):
    # n! can also be defined as n * (n-1)!
    """ calculate n! recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n -1)


def fib(n):
    """
    Fibonacci Numbers recursively
    F(n) = F(n - 1) + F(n - 2)
    """
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n):
    """
    Fibonacci Numbers recursively
    F(n) = F(n - 1) + F(n - 2)
    """
    result = -1
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result

    return result


for i in range(36):
    print(i, fib2(i), sep=": ")
























