class Director():

    """
    Director class is going to manage all the parts of the game

    Attributes:

    Author: Samuel Beltran
    """
    def __init__(self,videoService,script):
        self._video_service = videoService
        self._script = script
    
    def start_game(self):

        self._video_service.open_window()

        while self._video_service.is_playing():
            """ self.__execute_script("input")   
            """
            self.__execute_script("update")
            self.__execute_script("output")
        self._video_service.close_window()
    
    def __execute_script(self,actionName):

        self.__execute_action(self._script.get_action(actionName))

    def __execute_action(self,script):
        for action in script:
            action.execute()
