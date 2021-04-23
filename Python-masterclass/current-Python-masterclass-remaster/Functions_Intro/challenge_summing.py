"""Write a function that takes two parameters. The first parameter should take a number and the second one should
string 'e' or 'o',
if the second parameter is e then it should sum up all the even values before that first parameter,
if the second parameter is o then it should sum up all the odd values before that first parameter,
and else if the second parameter is something else it should return -1
"""


# First solution - by me
def sum_eo1(number, string):
    total = 0
    if string == "e":
        ft = 2
        while ft < number:
            total += ft
            ft += 2
    elif string == "o":
        ft = 1
        while ft < number:
            total += ft
            ft += 2

    return total


# Second solution - by Udemy Instructor
def sum_eo2(n, t):
    """Sum even or odd numbers in range.

    Return the sum of even or odd natural numbers, in the range 1..n-1.

    :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
    :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
    :return: The sum of the even or odd numbers in the range.
            Returns -1 if `t` is not 'e' or 'o'.
    """
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


# Third Solution - by me
def sum_even_odd(n: int, t: str) -> int:
    total = 0
    start = -1
    if t == 'e':
        start = 2
    elif t == 'o':
        start = 1

    for i in range(start, n, 2):
        total += i
    return total








