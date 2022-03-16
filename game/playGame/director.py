class Director():

    """
    Director class is going to manage all the parts of the game

    Attributes:

    Author: Samuel Beltran
    """
    def __init__(self,videoService,script):
        self._video_service = videoService
        self._script = script
        self._is_playing = True
    
    def start_game(self):

        self._video_service.open_window()

        while self._video_service.is_playing():
            
            self.__execute_script("input")              
            self.__execute_script("update")
            self.__execute_script("output")

        self._video_service.close_window()
    
    def __execute_script(self,actionName):

        action = self._script.get_action(actionName)
        self.__execute_action(action)
        
        if actionName == "update":
            self.check_is_playing(action)    
        
        if actionName == "output":
            self.stop_game(action)

    def __execute_action(self,script):
        
        for action in script:
            action.execute()                
    
    def check_is_playing(self,action):
        for a in action:
            if not a.is_game_over():
                self._is_playing = False

    def stop_game(self,action):
        if not self._is_playing:
            for a in action:
                a.change_game_state(False)
