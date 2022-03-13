from game.gameLogistics.script import Script
from game.gameLogistics.keyboardControl import KeyboardControl
from game.gameLogistics.playerActions import PlayerActions
from game.gameLogistics.controlPlayers import ControlPlayers
from game.gameLogistics.videoServices import VideoServices
from game.gameLogistics.videoControl import VideoControl
from game.playGame.director import Director
from game.character.characterStorage import CharacterStorage
from game.character.player import Player
from game.character.banner import Banner


WIDTH = 900
HEIGHT = 600
GAME_NAME = "CYCLE"
FRAME = 12
CELL_SIZE = 15
FONT_SIZE = 15
BLACK = (3,3,3,1)
COLS = (WIDTH/CELL_SIZE)
ROWS = (HEIGHT/CELL_SIZE)
RED = (255,0,0,200)
def main():


    storage = CharacterStorage()
    script = Script()
    videoServices = VideoServices(WIDTH,HEIGHT,GAME_NAME,FRAME,CELL_SIZE,True)

    """ creates the character: """
    """ bannerOne = Banner()
    bannerTwo = Banner() """

    x = int((COLS/3)* CELL_SIZE)
    y = int((ROWS/2)* CELL_SIZE)
    mainBanner = Banner(x,int(HEIGHT/2),"",50,RED)
    """ playerOne = Player("@","playerOne",x,y,CELL_SIZE,FONT_SIZE)
    playerTwo = Player("@","playerTwo",x + (CELL_SIZE * 20),y,CELL_SIZE,FONT_SIZE)  """
    
    playerOneCollider = Player("o","playerOne",x,y+CELL_SIZE,CELL_SIZE,FONT_SIZE)
    playerTwoCollider = Player("o","playerTwo",x + (CELL_SIZE * 20),y,CELL_SIZE,FONT_SIZE) 
    playerOne = Player("@","playerOne",x,y,CELL_SIZE,FONT_SIZE)
    playerTwo = Player("@","playerTwo",x + (CELL_SIZE * 20),y,CELL_SIZE,FONT_SIZE) 

    storage.add_new_character("playerOne",playerOneCollider)
    storage.add_new_character("playerOne",playerTwoCollider)
    
    storage.add_new_character("playerOne",playerOne)
    storage.add_new_character("playerTwo",playerTwo)
    storage.add_new_character("mainBanner",mainBanner)
    
    """ storage.add_new_character("banner_one",bannerOne)
    storage.add_new_character("banner_two",bannerTwo) """

    script.add_action("input",KeyboardControl(storage))
    script.add_action("update",ControlPlayers(storage,CELL_SIZE))
    script.add_action("output",VideoControl(videoServices,storage))

    director = Director(videoServices,script)
    director.start_game()


main()