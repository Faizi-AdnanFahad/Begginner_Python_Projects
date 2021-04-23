from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
# The setdefault method returns the value of the key passed to it, if it doesn't exist it will return the second
# argument
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")

# Returns the same thing as setdefault method but it doesn't add the non-existent key to the dictionary
ketchup_quantity = pantry.get("ketchup", 0)
print(ketchup_quantity)

z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")

print()

print("`pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)

