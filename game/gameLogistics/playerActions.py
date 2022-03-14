from game.gameLogistics.playersTrail import PlayersTrail
from game.gameOver.gameOver import GameOver
from game.gameScore.score import Score
class PlayerActions():
    
    def __init__(self,characters,player,distance):
        self._characters = characters
        self._player = player
        self._distance = distance
        self._trail_appearance = "#"
        
    def get_players(self):
        return self._characters
    
    def movement(self,direction=""):
        
        playerTrail = PlayersTrail(self._player)
        
        self.__insert_new_trail(self.__add_new_trail(playerTrail))
        
        if direction == "x" or direction == "-x":
            if direction == "x":
                self.__move_in_x_position(self._player,1)

            else:
                self.__move_in_x_position(self._player,-1)

        if direction == "y" or direction == "-y":
            if direction == "y" :
                self.__move_in_y_position(self._player,1)
            else:
                self.__move_in_y_position(self._player,-1)

        if direction == "":            
            self.__move_in_y_position(self._player,-1)

        
    def __move_in_x_position(self,player,direction):
        if direction > 0:
            player.set_x_position(player.get_x_position() + self._distance) 
        else:
            player.set_x_position(player.get_x_position() - self._distance) 

    def __move_in_y_position(self,player,direction):
        if direction > 0:
            player.set_y_position(player.get_y_position() + self._distance)
        else:
            player.set_y_position(player.get_y_position() - self._distance)
        
    def __add_new_trail(self,playerTrail):
        return playerTrail.add_new_trail()
    
    def __insert_new_trail(self,trail):        
        index = self._characters.add_new_character(self._player.get_group_name(),trail)
        self.__change_previous_char(index)

    def turn_player(self):
        pass

    def __change_previous_char(self,index):
        
        if index > 1:         
            previous = self._characters.get_character(self._player.get_group_name())[index-1]
            current = self._characters.get_character(self._player.get_group_name())[index]
            previous.set_appearance(self._trail_appearance) 
            current.set_color(previous.get_color()) 

    def game_over(self,mainBanner):
        return GameOver(mainBanner).game_over()

    def lose_points(self,player,playerBanner):
        scoreControler = Score(1)
        score = scoreControler.lose_point(player.get_score())
        playerBanner.add_to_message(str(score))
        self.__player_lose_point(player,score)
        
    def __player_lose_point(self,player,score):
        player.set_score(score)
        
    def change_player_color(self,player,color):
        player = self._characters.get_character(player.get_group_name())
        for p in player:
            if p.get_appearance() == self._trail_appearance:
                p.set_color(color)
    
    """ def create_walls(self):
        #print(self._player.get_x_position())
        for i in range(self._player.get_x_position()):
            print(i) """