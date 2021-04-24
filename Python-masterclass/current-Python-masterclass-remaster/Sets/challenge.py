
text = input("Please enter a text: ")
#
# First Solution
# text_in_list = []
# for char in text:
#     if char not in "aeiou":
#         text_in_list.append(char)
#
# text_in_set = set(sorted(text_in_list))
# print(text_in_set)

# Second Solution
vowels = frozenset("aieou")
set_of_non_vowels = set(text).difference(vowels)
print(set_of_non_vowels)
