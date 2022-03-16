class Score:
    """ 
        this will add or substract to the players score 
        Attributes:
            __points (int) : The number of points
        Author: Karras        
    """

    def __init__(self, points):
        self._points = points

    def earn_point(self, score):
        """ Adds points to the actual score
            return: int
        """
        return score + self._points

    def lose_point(self, score):
        """ Substract from the actual score 
            return int
        """
        return score - self._points
