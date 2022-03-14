from game.gameLogistics.playerActions import PlayerActions
from game.gameLogistics.collision import Colission
from game.playGame.action import Action

class ControlPlayers(Action):
    
    def __init__(self,characterStorage,cellSize):
        self._characterStorage = characterStorage
        self._cell_size = cellSize
        self._is_playing = True

    def execute(self):

        """ Main banner """
        mainBanner = self._characterStorage.get_character("mainBanner")[0]
        whiteColor = (255,255,255,200)

        """ Playerone variables """
        collisionPlayerOne = Colission(self._characterStorage,"playerOne","playerTwo",0,0)
        playerOne = self._characterStorage.get_character("playerOne")[0]
        actionsPlayerOne = PlayerActions(self._characterStorage,playerOne,15)
        scoreBannerOne = self._characterStorage.get_character("scoreBannerOne")[0]
        
        """ Players two variables """
        collisionPlayerTwo = Colission(self._characterStorage,"playerTwo","playerOne",0,0)
        playerTwo = self._characterStorage.get_character("playerTwo")[0]
        actionsPlayerTwo = PlayerActions(self._characterStorage,playerTwo,15)
        scoreBannerTwo = self._characterStorage.get_character("scoreBannerTwo")[0]


        """ Player one behaviors """
        if playerOne.get_score() < 0 or playerTwo.get_score() < 0:

            self._is_playing = False        
           
        
        self.__run_self_collision(collisionPlayerOne,actionsPlayerOne,mainBanner)
        self.__run_self_collision(collisionPlayerTwo,actionsPlayerTwo,mainBanner)

        if self.__run_enemy_collision(collisionPlayerOne,playerOne,playerTwo):
            self.__lose_points(actionsPlayerOne,playerOne,scoreBannerOne)
            self.__change_player_color(actionsPlayerOne,playerOne,whiteColor)
        
        if self.__run_enemy_collision(collisionPlayerTwo,playerTwo,playerOne):
            self.__lose_points(actionsPlayerTwo,playerTwo,scoreBannerTwo)
            self.__change_player_color(actionsPlayerTwo,playerTwo,whiteColor)

        actionsPlayerOne.movement(playerOne.get_direction())
        actionsPlayerTwo.movement(playerTwo.get_direction())
        
    def __run_self_collision(self,collisionPlayer,actionsPlayer,mainBanner):
        if collisionPlayer.check_collision() == "itself" or collisionPlayer.check_collision() == "window":
            if actionsPlayer.game_over(mainBanner):
                self._is_playing = False

        
    def __run_enemy_collision(self,collisionPlayer,playerOne,playerTwo):
        if collisionPlayer.check_collision() == "enemy":
            newDirection = collisionPlayer.check_free_way(playerOne.get_position(),playerTwo.get_position(),playerOne.get_direction())
            if newDirection != False:
                playerOne.set_direction(newDirection)
                return True

    def __lose_points(self,playerActions,player,playerBanner):
        playerActions.lose_points(player,playerBanner)

    def __change_player_color(self,playerActions,player,color):
        playerActions.change_player_color(player,color)

    def is_game_over(self):
        return self._is_playing