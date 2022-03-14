from game.gameLogistics.playerActions import PlayerActions
from game.gameLogistics.collision import Colission
from game.playGame.action import Action

class ControlPlayers(Action):
    
    def __init__(self,playerStorage,cellSize):
        self._players = playerStorage
        self._cell_size = cellSize
        self._is_playing = True

    def execute(self):

        collisionPlaOne = Colission(self._players,"playerOne","playerTwo",0,0)
        playerOne = self._players.get_character("playerOne")[0]
        playerTwo = self._players.get_character("playerTwo")[0]
        mainBanner = self._players.get_character("mainBanner")[0]
        actionsPlayerOne = PlayerActions(self._players,playerOne,15)
        actionsPlayerTwo = PlayerActions(self._players,playerTwo,15)
        
        if collisionPlaOne.check_collision() == "itself" or collisionPlaOne.check_collision() == "window":
            if actionsPlayerOne.game_over(mainBanner):
                self._is_playing = False

        if collisionPlaOne.check_collision() == "enemy":
        
            newDirection = collisionPlaOne.check_free_way(playerOne.get_position(),playerTwo.get_position(),playerOne.get_direction())
            if newDirection != False:
                playerOne.set_direction(newDirection)
            
        actionsPlayerOne.movement(playerOne.get_direction())
        actionsPlayerTwo.movement(playerTwo.get_direction())
        
    def is_game_over(self):
        return self._is_playing