text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)
# Mapping
map_letter_capital = list(map(str.upper, text))
print(map_letter_capital)

# Mapping
words = [word.upper() for word in text.split(' ')]
print(words)
map_words_upper = list(map(str.upper, text.split(' ')))
print(map_words_upper)
