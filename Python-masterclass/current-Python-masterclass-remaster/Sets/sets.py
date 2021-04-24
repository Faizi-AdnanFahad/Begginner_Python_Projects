# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("-" * 40)
#
# wild_animals = set(["tiger", "lion", "panther", "elephant", "hare"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# empty_set = set()
# print(empty_set)
#
# even = set(range(0, 40, 2))
# print(even)
#
# square_tuple = {4, 6, 9, 16, 25}
# squares = set(square_tuple)
# print(squares)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# # Union
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
#
# print("-" * 40)
#
# # Intersection
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
#
# print("-" * 40)
#
# print("even minus square")
# print(sorted(even.difference(squares)))
# print(even - squares)
#
# print()
#
# print("square minus even")
# print(sorted(squares.difference(even)))
# print(squares - even)
#
#
# print("=" * 40)
#
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))


# even = set(range(0, 40, 2))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
#
# print(even)
# print(squares)

# print("Symmetric even minus square ")
# print(even.symmetric_difference(squares))  # removes elements that intersect and add those which doesn't
# # OR  its the set of all elements except those which intersect
#
# print("Symmetric squares minus even ")
# print(squares.symmetric_difference(even))

# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
#
# squares.discard(4)
# squares.discard(16)
# squares.discard(8)  # element doesn't exist, but because of discard an error won't be raised
# print(squares)
#
# # squares.remove(8)   # raised an error because the element doesn't exist
#
# try:
#     squares.discard(8)
# except KeyError:
#     print("The item 8 is not a member of the set")

even = set(range(0, 40, 2))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of squares")


a = frozenset(range(0, 100, 2))
print(a)






