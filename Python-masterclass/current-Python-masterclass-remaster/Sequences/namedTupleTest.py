from namedTuples import basic_plants_list, plants_list

print(plants_list[0])

# for plant in basic_plants_list:
#     print(plant[0])

for plant in plants_list:
    print(plant.scientific_name, plant[1], sep="------")  # plant[1]

print()

example = plants_list[1]
print(example)
example = example._replace(lifecycle='annual')
print(example)

# a = plants_list[0]
# for i in a:
#     print(i)

