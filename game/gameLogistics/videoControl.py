from game.playGame.action import Action

class VideoControl(Action):

    def __init__(self,videoServices,characters):
        self._videoServices = videoServices
        self._characters = characters
        self._is_playing = True

    def execute(self):
        walls = self._characters.get_character("windowWalls")
        self._videoServices.draw_all_banners(walls)
        self._videoServices.draw_banner(self._characters.get_character("scoreBannerOne")[0])
        self._videoServices.draw_banner(self._characters.get_character("scoreBannerTwo")[0])

        self._videoServices.start_drawing()
        if not self._is_playing:
            self._videoServices.draw_banner(self._characters.get_character("mainBanner")[0])
            
        else:
            
            self._videoServices.draw_all_characters(self._characters.get_character("playerOne"))
            self._videoServices.draw_all_characters(self._characters.get_character("playerTwo"))
            
        self._videoServices.stop_drawing()
    
    def change_game_state(self,state):
        self._is_playing = state
