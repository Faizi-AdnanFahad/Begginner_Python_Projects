class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3  # underscored indicates that it should not be called in this file
        self._level = 1
        self._score = 0

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
            self._score = (level - self._level) * 1000
            self._level = level
        else:
            print("Level can't be less than 1")

    level = property(_get_level, _set_level)
    live = property(_get_lives, _set_lives)

    # These @property will act like determining a getter and will help us to omit the property method which was done for
    # other attributes. (level and live)
    @property
    def score(self):
        return self._score

    # These @score.setter will act like determining a setter and will help us to omit the property method which was
    # done for other attributes. (level and live)
    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return f"Name: {self.name}, Lives: {self._lives}, Level: {self._level}, Score: {self._score}"

