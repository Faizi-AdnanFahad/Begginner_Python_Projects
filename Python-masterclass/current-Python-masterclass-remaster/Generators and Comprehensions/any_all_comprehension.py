from data import people, basic_plants_list, plants_list, people, plants_dict

if all([person[1] for person in people]):
    print('Sending email')
else:
    print('User must edit the list of recipients')

# for emails in people[1]:
#     if "" in emails:
#         print("Failed")
#         break
#     else:
#         print('Success')

if any([plant.plant_type == 'Grass' for plant in plants_list]):
    print('This pack contains grass')
else:
    print('No grasses in this pack')


if any(([values.plant_type == 'Grass' for values in plants_dict.values()])):  # Generators used
    # ([values.plant_type == 'Grass' for values in plants_dict.values()])  Comprehensions used
    print('This dict contains Grass')
else:
    print('No Grasses in the dict')















