from game.gameLogistics.keyboard import Keyboard
from game.playGame.action import Action

class KeyboardControl(Action):
    
    def __init__(self,charStorage):
        self._character_storage = charStorage
        
    def execute(self):
        
        keyboard = Keyboard()
    
        playerOne = self._character_storage.get_character("playerOne")[0]
        playerTwo = self._character_storage.get_character("playerTwo")[0]        

        if playerOne.get_axis() == "" or playerTwo.get_axis() == "":
                playerOne.set_axis("y")
                playerTwo.set_axis("y")
    
        if keyboard.is_key_pressed():  
            
            keyboard.get_input()

            direction = keyboard.get_direction() + keyboard.get_axis()
            
            if keyboard.get_player() == 1:                
                if playerOne.get_axis() != keyboard.get_axis():
                    playerOne.set_axis(keyboard.get_axis()) 
                    playerOne.set_direction(direction)

            if keyboard.get_player() == 2:
                if playerTwo.get_axis() != keyboard.get_axis():
                    playerTwo.set_axis(keyboard.get_axis()) 
                    playerTwo.set_direction(direction)