from game.character.player import Player

class PlayersTrail:
    
    def __init__(self,player,color=""):
        self._player = player
        self._color = color

    def add_new_trail(self):
        x = self._player.get_x_position()
        y = self._player.get_y_position()
        
        return Player("@","trail",x,y,15,15,self._color)
        
