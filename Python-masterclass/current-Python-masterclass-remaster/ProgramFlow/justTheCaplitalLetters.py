quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.

# Solution 1
uppperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in quote:
    if char in uppperLetters:
        print(char)


print("-" * 50)

# Solution 2

for char in quote:
    if char.isupper():
        print(char)