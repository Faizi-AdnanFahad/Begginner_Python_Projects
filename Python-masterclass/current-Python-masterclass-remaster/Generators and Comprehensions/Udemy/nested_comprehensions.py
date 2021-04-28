# burgers = ['beef', 'chicken', 'spicy bean']
# toppings = ['cheese', 'egg', 'beans', 'spam']
# Comprehension
# burger_types = [(burger, topping) for burger in burgers for topping in toppings]
# print(burger_types)
# # Normal For loop
# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))
# # Looping over a comprehension list
# for meal in [(burger, topping) for burger in burgers for topping in toppings]:
#     print(meal)

burgers = ['beef', 'chicken', 'spicy bean']
toppings = ['cheese', 'egg', 'beans', 'spam']
for meal in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(meal)

print()

for meal in [[(burger, topping) for topping in toppings] for burger in burgers]:
        #    ------------------------------------------- **********************
        #                       Exressions                 *first iterations gets evaluated and the all iterations of expression gets evaluated*

    print(meal)























