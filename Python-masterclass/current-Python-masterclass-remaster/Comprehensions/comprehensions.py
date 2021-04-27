from typing import List

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Adding all elements of the nums to a new empty list
# *Normal way*
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# Using comprehensions
my_list = [n for n in nums]
print(my_list)

print("-----------------------------------------------------------------")

# Get the squares of each number in a list and adding them to a new_list
# Normal way
# square_list = []
# for n in nums:
#     square_list.append(n * n)
# print(square_list)

# Using Comprehensions
# square_list = [n*n for n in nums]
# print(square_list)

print("-----------------------------------------------------------------")

# creating a list for each n in nums if n is even
# Using normal For loop
# even_list = []
# for n in nums:
#     if n % 2 == 0:
#         even_list.append(n)
# print(even_list)

# Using Comprehension
# even_list = [n for n in nums if n % 2 == 0]
# print(even_list)

print("-----------------------------------------------------------------")

# I want a (letter, num) pair for each letter in `abcd` and each number in `0123`
# Using normal For loop
# my_list_pair = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list_pair.append((letter, num))
# print(my_list_pair)

# Using Comprehension

my_list_pair = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list_pair)

print("-----------------------------------------------------------------")

# Dictionary Comprehensions
names = ['Bruce', 'Clerk', 'Peter', 'Logan', 'Wada']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# zip function will create a list of tuples where each elements[index] consist of a pair of values from each list,
# in other words, indices as pairs which they match
# Using normal for loop
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)

# Using Comprehension
# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)

# what if we don't want peter to be included
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)

print("-----------------------------------------------------------------")

# Normal for loop
# nums = [1, 2, 3, 4, 1, 1, 3, 3, 4, 6, 7, 7, 7]
# new_set = set()
# for n in nums:
#     new_set.add(n)
# print(new_set)

# Comprehensions
# new_set = {n for n in nums}
# print(new_set)

print("-----------------------------------------------------------------")

# Generators
nums = [1, 2, 3, 4, 1, 1, 3, 3, 4, 6, 7, 7, 7]


# by Creating a function and storing its value to a number
def gen_func(ns: List[float]):
    for n in ns:
        yield n * n


my_gen = gen_func(nums)

for i in my_gen:
    print(i)
print("--------------------------------")

# Using Generators
squares_generators = (n * n for n in nums)
for i in squares_generators:
    print(i)

print("-----------------------------------------------------------------")













