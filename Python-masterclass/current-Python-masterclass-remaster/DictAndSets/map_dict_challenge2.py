locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {
    0: {"Q": 0},
    1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    2: {"N": 5, "Q": 0},
    3: {"W": 1, "Q": 0},
    4: {"N": 1, "W": 2, "Q": 0},
    5: {"W": 2, "S": 1, "Q": 0},
}

direction_dict = {
    "QUIT": "Q",
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W",
}

loc = 1


while True:
    print(locations[loc])
    available_direction = "-".join(exits[loc].keys())

    direction = input(f"Which direction do you want to go? {available_direction}").upper()

    if len(direction) == 1:  # more than one letter
        if direction == "Q":
            print(locations[0])
            break

        if direction in available_direction:
            loc = exits[loc][direction]
        else:
            print("You cannot go to that direction")
    elif len(direction) > 1:
        words = direction.split(" ")
        for word in words:
            if word in direction_dict:
                if word != "QUIT":
                    direction_in_words = direction_dict[word]
                    loc = exits[loc][direction_in_words]
                else:
                    break
        # OR
        # for word in direction_dict:  # checking ig other words which includes our initialized words in direction_dict
        #     if word in direction:
        #         if word != "QUIT":
        #             direction_in_words = direction_dict[word]
        #             loc = exits[loc][direction_in_words]
        #         else:
        #             print(locations[0])
        #             break




