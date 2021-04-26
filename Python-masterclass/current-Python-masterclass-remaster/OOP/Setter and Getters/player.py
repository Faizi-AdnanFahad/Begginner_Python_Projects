class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3  # underscored indicates that it should not be called in this file
        self._level = 1
        self.score = 0

    # Getter -  # underscored indicates that it should not be called in this file
    def _get_lives(self):
        return self._lives

    # Setter -  # underscored indicates that it should not be called in this file
    def _set_lives(self, lives):
        if lives > 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            self.score = (level - self._level) * 1000
            self._level = level
        else:
            print("Level can't be less than 1")

    # Used to set getters and setters to work and can be used using only one variable
    # setters can be used: contextObject.level = int(num)
    # getters can be used: var = contextObject.level
    # If we don't use the property function below, getters and setters will not be created
    level = property(_get_level, _set_level)

    live = property(_get_lives, _set_lives)

    def __str__(self):
        return f"Name: {self.name}, Lives: {self._lives}, Level: {self._level}, Score: {self.score}"

