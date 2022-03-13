from game.playGame.action import Action

class VideoControl(Action):

    def __init__(self,videoServices,characters):
        self._videoServices = videoServices
        self._characters = characters
        self._is_playing = True

    def execute(self):
        """ banner_one
        banner_two """
        self._videoServices.start_drawing()
        if not self._is_playing:
            self._videoServices.draw_banner(self._characters.get_character("mainBanner")[0])
            
        else:
            self._videoServices.draw_all_characters(self._characters.get_character("playerOne"))
            self._videoServices.draw_all_characters(self._characters.get_character("playerTwo"))

        self._videoServices.stop_drawing()
    
    def change_game_state(self,state):
        self._is_playing = state
