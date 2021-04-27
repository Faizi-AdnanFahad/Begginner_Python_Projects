# Operations on Strings
message = 'Hello World'
print(message.count('H'))
print(message.count('o'))
print(message.find('o'))  # First Occurrence - index 4
print(message.find('x'))  # -1 if it doesn't exist
print(message.replace('H', 'N'))  # Nello World

print("-----------------------------------------------------------")

# Operation on lists
a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list.count('H'))  # 0
print(a_list.count('o'))  # 0
print(a_list.index('b'))  # 1


