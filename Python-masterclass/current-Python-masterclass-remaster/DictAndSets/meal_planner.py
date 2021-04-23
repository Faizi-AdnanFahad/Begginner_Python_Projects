from contents import pantry, recipes

# display_dact = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dic = {}
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
        selected_item = display_dic[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients....")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"You need to buy: {quantity_to_buy} of {food_item}")










