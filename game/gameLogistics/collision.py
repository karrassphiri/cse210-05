class Colission:
    """ this is in charge of the collision of the players 

    Author: Karrass
    """

    def __init__(self, characters, score, points):
        self._characters = characters
        self._score = score
        self._points = points

    def check_collision(self):
        """Checks if the player is colliding with an object.

        Args:
            self (self): The cast of characters."""

        score = score(self._points)
        player = self._characters.get_character("player")[0]
        gems = self._characters.get_character("gem")
        rocks = self._characters.get_character("rock")

        for gem in gems:
            if self.__is_colliding(player, gem):
                self._score = score.earn_point(self._score)

        for rock in rocks:
            if self.__is_colliding(player, rock):
                self._score = score.lose_point(self._score)

    def __is_colliding(self, player, character):
        """ Evaluates if the player has the same position as the current character
            return: bool
        """
        if character.equals(character.get_position(), player.get_position()):
            return True

    def get_score(self):
        """ Gets the score
            return: int
        """
        return self._score
