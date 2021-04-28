from typing import List

nums = [1, 2, 3, 4, 5]
# # Creating generators using a function


def square_numbers(nums: List[float]):
    for i in nums:
        yield i * i


my_list = square_numbers(nums)  # [1, 4, 9, 16, 25]
print(next(my_list))  # 1
print(next(my_list))  # 4
print(next(my_list))  # 9
print(next(my_list))  # 16
print(next(my_list))  # 25

# Creating generators - easy
# nums = [1, 2, 3, 4, 5]
# my_generator_num = (n * n for n in nums)
# # print(my_generator_num)  # <generator object <genexpr> at 0x000002A6A65E7120>
# # creating a list of generators
# # my_generator_list = list(my_generator_num)  # [1, 4, 9, 16, 25]
# # print(my_generator_list)
# for n in my_generator_num:
#     print(n)



















