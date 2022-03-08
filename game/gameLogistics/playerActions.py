from game.playGame.action import Action
class PlayerActions(Action):
    
    def __init__(self,character):
        self._character = character
        
        
    def test(self):
        print("this is a test")
        
    def execute(self):
        print("this will excutate all the behaviors of the player")