from player2 import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing

# PLAYER CLASS
# tim = Player("Tim")

# ENEMY CLASS
# random_monster = Enemy("Basic enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(8)
# print(random_monster)
#
# random_monster.take_damage(9)
# print(random_monster)

# TROLL CLASS
# ugly_troll = Troll("Pug")
# print(f"Ugly troll = {ugly_troll}")  # __str__ method will cause the new object to be called alone and the code
# in the body of that to be stored in the new object variable.


# print("-------------------")
# brother = Troll("Urg")
# print(brother)
# brother.take_damage(10)
# print(brother)
#
# ugly_troll.grunt()
# brother.grunt()
#
#
# print("-------------------------------------------------------------")
#
# another_troll = Troll("Ug")  # initial points = 23
# print(f"Another troll = {another_troll}")
# another_troll.grunt()
# another_troll.take_damage(18)
# print(another_troll)
# another_troll.take_damage(30)
# print(another_troll)
#
# print("-------------------------------------------------------------")
#
# vamp = Vampyre("Vlad")
# print(vamp)
# vamp.take_damage(5)
# print(vamp)
# # while vlad.alive:
# #     vlad.take_damage(1)
# #     # print(vlad)

print("-------------------------------------------------------------")

dracula = VampyreKing("Dracula")
dracula.take_damage(12)
print(dracula)





































