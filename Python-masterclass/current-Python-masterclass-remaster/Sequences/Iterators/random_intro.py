import random

# value = random.random()  # between 0 and 1
# print(value)

# value = random.uniform(1, 10)   # random `floating number` between a range

# GOOD METHODS
# 1
value = random.randint(0, 1)
print(value)

# 2
# greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
# print(random.choice(greetings))

# 3
colors = ['Red', 'Black', 'Green']
print(random.choices(colors, k=10))  # a list of random values with the number of k
print(random.choices(colors, weights=[18, 18, 2], k=10))  # In this example, 'Red' = (18/18+18+2) chances,
# 'Black' = (18/18+18+2) chances, `Green` = (2/18+18+2) chances of being randomly selected.

# 4

deck = list(range(1, 53))
print(deck)
random.shuffle(deck)
print(deck)


# to pick random cards number from the list repeatedly, *NOTE* we can't use .choice or .choices method because can
# return repeated values
hand = random.sample(deck, k=5)
print(hand)













