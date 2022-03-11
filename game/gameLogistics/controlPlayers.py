from game.gameLogistics.playerActions import PlayerActions
from game.playGame.action import Action

class ControlPlayers(Action):
    
    def __init__(self,playerStorage,cellSize):
        self._players = playerStorage
        self._cell_size = cellSize

    def execute(self):
        actionsPlayerOne = PlayerActions(self._players,self._players.get_character("playerOne")[0],12)
        actionsPlayerTwo = PlayerActions(self._players,self._players.get_character("playerTwo")[0],12)
        actionsPlayerOne.movement()
        actionsPlayerTwo.movement()
