from contents import pantry, recipes


def list_of_required_items(dict_of_ingredients: dict) -> dict:
    """add the items with the amount needed for the meal"""
    required_ingredients = {}
    for item, number_of_items_needed in dict_of_ingredients.items():
        quantity_in_pantry = pantry.get(item, 0)
        if quantity_in_pantry < number_of_items_needed:
            quantity_to_buy = number_of_items_needed - quantity_in_pantry
            required_ingredients[item] = quantity_to_buy

    return required_ingredients


def list_of_items_that_are_ok(dict_of_ingredients: dict) -> list:
    """add items to that have enough ingredients for meal"""
    list_of_ok_items = []
    for item, number_of_items_needed in dict_of_ingredients.items():
        quantity_in_pantry = pantry.get(item, 0)
        if quantity_in_pantry >= number_of_items_needed:
            list_of_ok_items.append(item)
    return list_of_ok_items


# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dic = {}
shopping_list = {}  # Things to buy
previous_item = 0
for index, key in enumerate(recipes):
    display_dic[str(index + 1)] = key

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipes")
    print("---------------------------")
    for key, value in display_dic.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dic:
        selected_item = display_dic[choice]  # meal
        print(f"You have selected {selected_item}")
        print("checking ingredients....")
        ingredients = recipes[selected_item]  # ingredients of meal and its required item
        dict_to_buy = list_of_required_items(ingredients)
        for required_item in dict_to_buy:
            previous_item += int(dict_to_buy[required_item])
            shopping_list[required_item] = previous_item
            print(required_item)
        print(dict_to_buy)
        list_ok = list_of_items_that_are_ok(ingredients)
        print(list_ok)

for item, required_value in shopping_list.items():
    print(item, required_value, sep=": ")







