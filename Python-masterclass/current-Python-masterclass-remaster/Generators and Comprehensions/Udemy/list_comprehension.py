print(__file__)

number = int(input("Please enter a number, and I'll tell you its square: "))
numbers = [1, 2, 3, 4, 5, 6]
dictt = {"one": 1, "two": 2, "three": 3, "four": 4}

squares = [number ** 2 for number in numbers]  # List Comprehension
# set_square = {number ** 2 for number in numbers}  # Set Comprehension
# squares = [number ** 2 for number in range(1, 7)]
# print(squares)
index_pos = numbers.index(number)
print(squares[index_pos])



























