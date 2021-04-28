
def odd_gen():
    n = - 1
    while True:
        n += 1
        yield 2 * n + 1


# My solution
# def pi_series():
#     odds = odd_gen()
#     approximation = 0
#     var = 0
#     while True:
#         if var % 2 == 0:
#             approximation += (1 / next(odds))
#             print(4 * approximation)
#             var += 1
#         elif var % 2 == 1:
#             approximation -= (1 / next(odds))
#             print(4 * approximation)
#             var += 1


def pi_series():
    odds = odd_gen()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


a = pi_series()

for i in range(100000000):
    print(next(a))






