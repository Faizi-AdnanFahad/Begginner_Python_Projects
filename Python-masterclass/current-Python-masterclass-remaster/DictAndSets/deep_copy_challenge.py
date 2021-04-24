from contents import recipes


def deep_copy_dict(dictionary: dict) -> dict:
    """Creates a `deep copy` of the given dictionary"""
    dict_deep_copied = {}
    for keys, values in dictionary.items():
        copy_value = values.copy()
        dict_deep_copied[keys] = copy_value

    return dict_deep_copied


recipes_copy = deep_copy_dict(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])