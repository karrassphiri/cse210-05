from game.gameLogistics.keyboard import Keyboard
from game.playGame.action import Action

class KeyboardControl(Action):
    
    def __init__(self,charStorage):
        self._character_storage = charStorage
        
    def execute(self):
        print("from keyboardControl: all the behaviors of the keyboard will be executed")