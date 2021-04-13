#   immutable can't be changed, with the need to create a new id in the memory
# immutable:
    # result = True
    # another_result = result
    # print(id(result))
    # print(id(another_result))
    #
    # result = True
    # print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

# Results will have different ids at this point because its immutable
result += "ish"
print(id(result))

result = "ish"
print(id(result))

