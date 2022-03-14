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
WHITE = (255,255,255,200)
COLS = (WIDTH/CELL_SIZE)
ROWS = (HEIGHT/CELL_SIZE)
RED = (255,0,0,200)
SCORE = 3

def main():


    storage = CharacterStorage()
    script = Script()
    videoServices = VideoServices(WIDTH,HEIGHT,GAME_NAME,FRAME,CELL_SIZE)

    """ creates the character: """
    """ bannerOne = Banner()
    bannerTwo = Banner() """

    x = int((COLS/3)* CELL_SIZE)
    y = int((ROWS/2)* CELL_SIZE)
    mainBanner = Banner(x,int(HEIGHT/2),"",50,RED)
    scoreBannerOne = Banner(0,0,"Player one: ",20,WHITE)
    scoreBannerOne.add_to_message(str(SCORE))
    scoreBannerTwo = Banner(int((COLS*12)),0,"Player two: ", 20, WHITE)
    scoreBannerTwo.add_to_message(str(SCORE))

    playerOne = Player("0","playerOne",x,y+CELL_SIZE,FONT_SIZE,CELL_SIZE,BLACK,SCORE)
    playerTwo = Player("0","playerTwo",x + (CELL_SIZE * 20),y,FONT_SIZE,CELL_SIZE,BLACK,SCORE) 

    storage.add_new_character("playerOne",playerOne)
    storage.add_new_character("playerTwo",playerTwo)
    storage.add_new_character("mainBanner",mainBanner)
    storage.add_new_character("scoreBannerOne",scoreBannerOne)
    storage.add_new_character("scoreBannerTwo",scoreBannerTwo)

    script.add_action("input",KeyboardControl(storage))
    script.add_action("update",ControlPlayers(storage,CELL_SIZE))
    script.add_action("output",VideoControl(videoServices,storage))

    director = Director(videoServices,script)
    director.start_game()


main()