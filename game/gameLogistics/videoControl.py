from game.playGame.action import Action

class VideoControl(Action):

    def __init__(self,videoServices):
        self._videoServices = videoServices

    def execute(self):
        print("from videoControl : All the behaviors of the video will be executed")    