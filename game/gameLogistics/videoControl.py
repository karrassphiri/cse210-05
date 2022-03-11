from game.playGame.action import Action

class VideoControl(Action):

    def __init__(self,videoServices,characters):
        self._videoServices = videoServices
        self._characters = characters

    def execute(self):
        """ banner_one
        banner_two """
        self._videoServices.start_drawing()
        self._videoServices.draw_all_characters(self._characters.get_character("player_one"))
        self._videoServices.draw_all_characters(self._characters.get_character("player_two"))
        self._videoServices.stop_drawing()