shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "eggs"
found_at = None

# Method 1
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break


# Method 2
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at != None:
    print(f"Item fount at index {found_at}")
else:
    print(f"{item_to_find} not found")

# Method 3
# for item in shopping_list:
# found_at = -1
#     if item == "spam":
#         found_at = found_at + 1
#         break
#     found_at = found_at + 1
#
# print(found_at)

#   for index in range(6):
