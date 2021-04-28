menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(meals)

# Using Comprehension
# only taking the meals without spam
meals1 = [meal for meal in menu if 'spam' not in meal]
# only taking meals without spam or chicken
meals2 = [meal for meal in menu if 'spam' not in meal if 'chicken' not in meal]
meals3 = [meal for meal in menu if 'spam' not in meal and 'chicken' not in meal]

print(meals1)
print(meals3)

fussy_meal1 = [meal for meal in menu if 'spam' in meal or 'eggs' in meal if not ('bacon' in meal and 'sausage' in meal)]
fussy_meal2 = [meal for meal in menu if
               ('spam' in meal or 'eggs' in meal) and not ('bacon' in meal and 'sausage' in meal)]
print(fussy_meal1)
print(fussy_meal2)
