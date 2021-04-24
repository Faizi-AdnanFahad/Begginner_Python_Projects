pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
}

a = pantry.get("chicken", "We don't have that")
print(a)  # If we have the key chicken, `a` will be -> 500. else, if the key doesn't exist, then the second arguement
#           will be stored in `a`

# Sorting the keys of a dictionary
sorted_keys = list(pantry.keys())  # OR # sorted_keys = sorted(list(pantry.keys())
sorted_keys.sort()
for f in sorted_keys:
    print(f, pantry[f])
