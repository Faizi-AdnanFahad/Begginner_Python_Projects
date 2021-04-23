available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
computer_parts = {}  # create an empty dictionary
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice not in computer_parts:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        else:
            print(f"Removing {chosen_part}")
            del computer_parts[current_choice]  # computer_parts.pop(current_choice)
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        print("Please add options from the list: ")
        for key, value in available_parts.items():
            print(key, value, sep=": ")
            # print(f"{key}: {value}")

    current_choice = input("> ")

