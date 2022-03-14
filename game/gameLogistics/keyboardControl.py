from game.gameLogistics.keyboard import Keyboard
from game.playGame.action import Action

class KeyboardControl(Action):
    
    def __init__(self,charStorage):
        self._character_storage = charStorage
        
    def execute(self):
        
        """ keyboardOne = Keyboard()
        keyboardTwo = Keyboard()
        
        playerOne = self._character_storage.get_character("playerOne")[0]
        playerTwo = self._character_storage.get_character("playerTwo")[0]        
        if keyboardOne.get_input(1) != "":
            playerOne.set_direction(keyboardOne.get_input(1))
            
        if keyboardTwo.get_input_two(2) != "":    
            playerTwo.set_direction(keyboardTwo.get_input_two(2)) """

        keyboard = Keyboard()
    
        playerOne = self._character_storage.get_character("playerOne")[0]
        playerTwo = self._character_storage.get_character("playerTwo")[0]        
        #print(keyboard.get_input(1) != "")
        if keyboard.is_key_pressed():
            keyboard.get_input()
            
            if keyboard.get_player() == 1:
                playerOne.set_direction(keyboard.get_input())
            if keyboard.get_player() == 2:
                playerTwo.set_direction(keyboard.get_input())
            #print(keyboard.get_input(2))
            #playerOne.set_direction(keyboardOne.get_input(1))

        
        """ if keyboard.get_input(2) != "":    
            playerTwo.set_direction(keyboard.get_input_two(2)) """