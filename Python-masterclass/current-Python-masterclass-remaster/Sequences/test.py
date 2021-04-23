Numbers = {"one": 1, "two": 2, "three": 3}
Numbers["one"] = Numbers.setdefault("one", 0) + 80
# returns 0 if the key doesn't exist in dictionary Numbers
print(Numbers)  # -> {'one': 81, 'two': 2, 'three': 3}
