shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     print("Buy " + item)

# what if we don't want to print "spam"?
# 1
for item in shopping_list:
    if item != "spam":
        print(item)

print()

# 2
for item in shopping_list:
    if item == "spam":
        continue

    print("Buy " + item)

# for i in range(0, len(shopping_list)):
#     print(shopping_list[i])

print("---------------Usage of Break-----------------")
for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)