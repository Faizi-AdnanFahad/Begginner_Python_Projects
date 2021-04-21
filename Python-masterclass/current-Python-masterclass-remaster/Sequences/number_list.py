empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

# creating another list (copying) another number's list - without any modification to the numbers

# Copying lists
#   1
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

print("-------------------------------------")

#-------------------- EXTRA----------------
digits1 = sorted("432985617")   # it will sort the list and create a new list
print(digits1)
#------------------------------------------

print("-------------------------------------")

#   2
digits = list("432985617")      # it will create ANOTHER list from this string literal
print(digits)
print(numbers)

print("-------------------------------------")

#   3
more_numbers = list(numbers)    # creates another list
print(more_numbers)
print(numbers)
print(numbers is more_numbers)

print("-------------------------------------")

#   4
more_numbers2 = numbers[:]
print(more_numbers2)
print(numbers)

#   5
more_numbers5 = numbers.copy()
print(more_numbers5)
print(numbers)
print(numbers is more_numbers5)

print("---------------------------------------------")

#   6   MOST EFFICIENT
more_numbers6 = [*numbers]
print(more_numbers6 is numbers)

print("---------------------------")

#   7
more_numbers7 = numbers.copy()
print(more_numbers7 is numbers) #   *is* operator returns true if both lists are pointing to the same address
print(more_numbers7 == numbers) #   == operator will return true if both lists contain the same elements with the same order









# even.extend(odd)
# print(even)
#
# another_even = even
# print(another_even)
#
# even.sort(reverse=True)
# print(even)
# print(another_even)

