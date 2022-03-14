from operator import invert
import pyray

class Colission:
    """ this is in charge of the collision of the players 

    Author: Karrass
    """

    def __init__(self, characters,playerName,enemyName,score, points):
        self._characters = characters
        self._player_name = playerName
        self._enemy_name = enemyName
        self._score = score
        self._points = points
        self._count = 0

    def check_collision(self):
        
        """Checks if the player is colliding with an object.

        Args:
            self (self): The cast of characters."""

        value = ""
        player = self._characters.get_character(self._player_name)
        enemy = self._characters.get_character(self._enemy_name)

        if self.__check_itself_collision(player):
            value = "itself"

        if self.__check_windows_limits_collision(player):
            value = "window"

        if self.__check_enemy_collision(player,enemy):
            value = "enemy"

        return value

    def __check_itself_collision(self,player):

        """ if len(player) > 5: 
            for p in player:
                if p.get_appearance() != player[0].get_appearance():
                    if self.__is_colliding(player[0],p):
                        return True """
        if len(player) > 5: 
            for p in player:
                
                if p.get_appearance() != player[0].get_appearance():
                    if self.__is_colliding(player[0],p):
                        
                        return True
        

    def __check_enemy_collision(self,player,enemy):
        
        for e in enemy: 
            if self.__is_colliding(player[0],e) != None:
                return self.__is_colliding(player[0],e)
            

    def __check_windows_limits_collision(self,player):
        
        if player[0].get_x_position() < 20 or player[0].get_x_position() > 880:
            return True

        if player[0].get_y_position() < 20 or player[0].get_y_position() > 580:
            return True
            

    def __is_colliding(self, player, character):
        """ Evaluates if the player has the same position as the current character
            return: bool
        """
        if player.equals(player.get_position(),character.get_position()):
            """ print(player.get_x_position(),player.get_y_position())
            print(character.get_x_position(),character.get_y_position()) """
            return True

    def get_score(self):
        """ Gets the score
            return: int
        """
        return self._score

    def check_free_way(self,playerPosition,enemyPosition,playerDirection):

        player = self._characters.get_character(self._player_name)
        enemy = self._characters.get_character(self._enemy_name)
        newDirection = ""
        for p in player:
            if playerDirection == "y" or playerDirection == "-y":

                if (player[0].get_x_position()+ 15) != p.get_x_position():
                    for e in enemy:
                        if (player[0].get_x_position()+ 15) !=  e.get_x_position():
                            if e.get_x_position() > (player[0].get_x_position() + 60):
                                newDirection = "x"
                            else:
                                newDirection = "-x"
                else:
                    newDirection = False

            if playerDirection == "x" or playerDirection == "x":    
                if (player[0].get_y_position()+ 15) != p.get_y_position():
                    for e in enemy:
                        if (player[0].get_y_position()+ 15) !=  e.get_y_position():
                            if e.get_y_position() > (player[0].get_y_position() + 60):
                                newDirection = "y"
                            else:
                                newDirection = "-y"
                else:
                    newDirection = False

            return newDirection
            """ if p.get_x_position() != playerPosition.get_x_position() and p.get_x_position() != enemyPosition.get_x_position():
                print("libre en x")
            if p.get_y_position() != playerPosition.get_y_position() and p.get_y_position() != enemyPosition.get_y_position():
                print("free in y") """