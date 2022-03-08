class Director:

    """
    Director class is going to manage all the parts of the game

    Attributes:

    Author: Samuel Beltran
    """
    def __init__(self,videoService,script):
        self._video_service = videoService
        self._script = script
    
    def start_game(self,storage):

        self._video_service.open_window()

        while self._video_service.is_playing():
            self._script.get_action("update")[0].test()
                
        self._video_service.close_window()