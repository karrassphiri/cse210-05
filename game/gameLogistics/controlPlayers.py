from game.gameLogistics.playerActions import PlayerActions
from game.playGame.action import Action

class ControlPlayers(Action):
    
    def __init__(self,playerStorage):
        self._players = playerStorage

    def execute(self):
        playerActions = PlayerActions(self._players)
        print("from controlPlayers: here we will control all the players n¿behavior")
