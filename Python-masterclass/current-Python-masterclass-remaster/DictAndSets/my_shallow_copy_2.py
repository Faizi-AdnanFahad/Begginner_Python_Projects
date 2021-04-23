lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals2 = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

things = animals2.copy()

print(things["teddy"])  # ['cuddly', 'stuffed']
print(animals2["teddy"])  # ['cuddly', 'stuffed']

print()

# things["teddy"].append("toy") OR teddy_list.append("toy")
teddy_list.append("toy")
animals2["teddy"].append("added via `animals2`")
things["teddy"].append("added via `things`")
print(things["teddy"])  # ['cuddly', 'stuffed', 'toy']
print(animals2["teddy"])  # ['cuddly', 'stuffed', 'toy']











