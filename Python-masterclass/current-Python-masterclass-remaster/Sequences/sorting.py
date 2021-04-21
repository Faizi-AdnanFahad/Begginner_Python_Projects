pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_number = sorted(numbers)

print(numbers)
print(sorted_number)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumps over the lazy dog", key=str.casefold)
print(missing_letter)


names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]

names.sort()
print(names)
names.sort(key=str.casefold)

print(names)







