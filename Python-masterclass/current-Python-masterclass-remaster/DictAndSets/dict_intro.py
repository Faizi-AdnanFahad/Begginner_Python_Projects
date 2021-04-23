vehicles = {'dream': 'Honda 250T',
            'roadster': 'BMW R1100',
            'er5': 'Kawasaki ER5',
            'can-am': 'Bombardier Can-Am 250',
            'virago': 'Yamaha XV250',
            'tenere': 'Yamaha XT650',
            'jimny': 'Suzuki Jimny 1.5',
            'fiesta': 'Ford Fiesta Ghia 1.4',
            }

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# Upgrade the Virago
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", "You wish! Sell the Learjet and you might afford a racing car.")
print(result)  # --> "You wish! Sell the Learjet and you might afford a racing car."

plane = vehicles.pop("learjet")  # Deletes learjet key and the value of it is stored in plane
print(plane)

bike = vehicles.pop("tenere", "not present")
print()

# for key in vehicles:
#     print(key, vehicles[key], sep=": ")

for key, value in vehicles.items():
    print(key, value, sep=": ")

a = {1: "one", 2: "two"}
pop = a.pop(3, None)
# del a[1]  # --> a = {2: "two"}
print(pop)

# Notes: Print to confirm
# dictt = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
# print(dictt)
# deleted_item = dictt.pop(1)
# print(dictt)
# print(deleted_item)
#
# # non-existent key
# # print(8) --> error
#
# print(8, None)  # None


# # ******************IMPORTANT*******************
# # The key doesn't exist and the program crashes
# commuter = vehicles['VIRAGO']
# print(commuter)  # --> Crushes
#
# # The key doesn't exist and the program returns NONE
# learner = vehicles.get("err5")
# print(learner)  # --> None
