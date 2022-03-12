from game.gameLogistics.keyboard import Keyboard
from game.playGame.action import Action

class KeyboardControl(Action):
    
    def __init__(self,charStorage):
        self._character_storage = charStorage
        
    def execute(self):
        
        keyboard = Keyboard()
        playerOne = self._character_storage.get_character("playerOne")[0]
        #playerTwo = self._character_storage.get_character("playerTwo")[0]        
        if keyboard.get_input() != "":
            playerOne.set_direction(keyboard.get_input())

        #playerTwo.set_direction(keyboard.get_direction())