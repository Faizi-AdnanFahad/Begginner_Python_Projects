import random


class Enemy:  # OR # class Enemy(object)

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print(f"I took {damage} points damage and have {self.hit_points} left")
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f"{self.name} lost a life")
                self.hit_points = 12
            else:
                print(f"{self.name} is dead")
                self.alive = False

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit points: {self.hit_points}"


# Troll class inherit from its superclass Enemy
class Troll(Enemy):

    def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print(f"Me {self.name}. {self.name} stomp you")


class Vampyre(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print(f"***** {self.name} dodges *****")
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampyreKing(Vampyre):

    def __init__(self, name):
        super().__init__(name=name)  # this super class is referring to Vampyre not the enemy
        self.hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage=damage // 4)












