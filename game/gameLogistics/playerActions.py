from game.gameLogistics.playersTrail import PlayersTrail
from game.gameOver.gameOver import GameOver

class PlayerActions():
    
    def __init__(self,players,character,distance):
        self._players = players
        self._character = character
        self._distance = distance
        
    def get_players(self):
        return self._players
    
    def movement(self,direction=""):
        
        playerTrail = PlayersTrail(self._character,self._distance)
        
        self.__insert_new_trail(self.__add_new_trail(playerTrail))

        if direction == "x" or direction == "-x":
            if direction == "x":
                self.__move_in_x_position(1)

            else:
                self.__move_in_x_position(-1)

        if direction == "y" or direction == "-y":
            if direction == "y" :
                self.__move_in_y_position(1)
            else:
                self.__move_in_y_position(-1)

        if direction == "":            
            self.__move_in_y_position(-1)

        
    def __move_in_x_position(self,direction):
        if direction > 0:
            self._character.set_x_position(self._character.get_x_position() + self._distance) 
        else:
            self._character.set_x_position(self._character.get_x_position() - self._distance) 

    def __move_in_y_position(self,direction):
        if direction > 0:
            self._character.set_y_position(self._character.get_y_position() + self._distance)
        else:
            self._character.set_y_position(self._character.get_y_position() - self._distance)
        
    def __add_new_trail(self,playerTrail):
        return playerTrail.add_new_trail()
    
    def __insert_new_trail(self,trail):        
        self._players.add_new_character(self._character.get_group_name(),trail)

    def turn_player(self,playerPosition,enemyPosition):
        pass


    def game_over(self,mainBanner):
        return GameOver(mainBanner).game_over()
    