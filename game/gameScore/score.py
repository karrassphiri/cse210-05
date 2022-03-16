
class Score():
    """ 
        This will substract to the players score 
        Attributes:
            __points (int) : The number of points
        Author: Karras        
    """

    def __init__(self, points):
        self._points = 1
        

    def lose_point(self, score):
        """ Substract from the actual score 
            return int
        """
        if score != 0:
            return score - self._points
        elif score == 0:
            return score
        
