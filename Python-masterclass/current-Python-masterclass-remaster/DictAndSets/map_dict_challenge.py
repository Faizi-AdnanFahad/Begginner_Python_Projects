locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
direction_dict = {}
while True:
    print(locations[loc])
    available_direction = "-".join(exits[loc].keys())

    direction = input(f"Which direction do you want to go? {available_direction}").upper()

    if direction == "WEST":
        direction_dict[direction] = "W"
    elif direction == "SOUTH":
        direction_dict[direction] = "S"
    elif direction == "EAST":
        direction_dict[direction] = "E"
    elif direction == "NORTH":
        direction_dict[direction] = "N"

    if direction == "Q":
        print(locations[0])
        break

    if direction in direction_dict:
        direction_in_words = direction_dict[direction]
        loc = exits[loc][direction_in_words]
    else:
        print("You cannot go to that direction")









