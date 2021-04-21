menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for menu_list in menu:
    for indexMenu in range(len(menu_list) - 1, -1, -1):
        if menu_list[indexMenu] == "spam":
            del menu_list[indexMenu]
    #   print(menu_list) uncomment to better understand
    print(", ".join(menu_list))











# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=", ")  # end will print ", " after each line is printed insted if '\n'
#     print()

# menus = ""
# for menuL in menu:
#     menus += str(menu.index(menuL)) + "- "
#     for i in range(len(menuL)):
#         if i < len(menuL) - 1:
#             menus += menuL[i] + ", "
# print(menus)


# for mealListIndex in range(len(menu)):
#     for indexMeal in range(len(menu[mealListIndex]) - 1, -1, -1):
#         if menu[mealListIndex][indexMeal] == "spam":
#             print(indexMeal)
