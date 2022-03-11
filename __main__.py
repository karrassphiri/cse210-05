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
def main():


    storage = CharacterStorage()
    script = Script()
    videoServices = VideoServices(WIDTH,HEIGHT,GAME_NAME,FRAME,CELL_SIZE)

    """ creates the character: """
    playerOne = Player("@","playerOne",210,210,15,15)
    playerTwo = Player("@","playerTwo",610,210,15,15)
    bannerOne = Banner()
    bannerTwo = Banner()

    storage.add_new_character("player_one",playerOne)
    storage.add_new_character("player_two",playerTwo)
    storage.add_new_character("banner_one",bannerOne)
    storage.add_new_character("banner_two",bannerTwo)

    #print(storage)
    script.add_action("input",KeyboardControl(storage))
    script.add_action("update",ControlPlayers(storage))
    script.add_action("output",VideoControl(videoServices,storage))

    director = Director(videoServices,script)
    director.start_game()


main()