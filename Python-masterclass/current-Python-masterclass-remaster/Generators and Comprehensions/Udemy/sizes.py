import sys


def my_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1


# big_range = range(10000)
big_range = my_range(5)

print(next(big_range))  # 0
print(next(big_range))  # 1
print(next(big_range))  # 2
# At this point, 3 values of the variable from the function call has been exhausted
# Going forward only 2 values is remained to be used while using the variable big_range on any loop

print(f'big_range is {sys.getsizeof(big_range)} bytes')

# Create a list containing all the values in big_range
big_list = []
for val in big_range:
    big_list.append(val)

print(f"big_list is {sys.getsizeof(big_list)} bytes")
print(big_range)
print(big_list)

print("-----------------")
# print("Having every i value")
# for i in my_range(5):
#     print(f"i is {i}")

print("Nothing is remained to be looped, since all variable values of big_range is consumed")
for i in big_range:
    print(f"i is {i}")














