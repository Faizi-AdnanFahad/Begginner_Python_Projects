#   mutable can be changed, without the need to create a new id in the memory
shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list
print(shopping_list)
print(another_list)
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(id(shopping_list))
print(another_list)
print(id(another_list))

a = b = c = d = e = f = another_list
print(a)

print("Adding cream")
b.append("cream")
print(a)
print(b)
